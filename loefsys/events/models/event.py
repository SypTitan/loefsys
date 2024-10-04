"""In this module, the models for events are defined.

Two types of events exist. Events with mandatory registration are defined by
:class:`.RequiredRegistrationEvent` and events with optional registration are defined by
the regular :class:`.Event`. Loefbijter currently does not organize any activities with
optional registration, so it is possible that this model gets deleted in the future.
"""

from datetime import datetime
from decimal import Decimal
from typing import override

from django.core import validators
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django_extensions.db.models import TimeStampedModel, TitleSlugDescriptionModel

from loefsys.contacts.models import Contact
from loefsys.events.models.choices import EventCategories, RegistrationStatus
from loefsys.events.models.managers import EventManager, EventRegistrationManager
from loefsys.groups.models import LoefbijterGroup


class Event(TitleSlugDescriptionModel, TimeStampedModel):
    """Model for an event.

    TODO @Mark expand on this.

    Attributes
    ----------
    created : ~datetime.datetime
        The timestamp of the creation of the model, automatically generated upon
        creation.
    modified : ~datetime.datetime
        The timestamp of last modification of this model, automatically generated upon
        update.
    title : str
        The title to display for the event.
    description : str, None
        An optional description of the event.
    slug : str
        A slug for the URL of the event, automatically generated from the title.
    organiser_groups : ~django.db.models.query.QuerySet of ~loefsys.groups.models.Group
        A query of all groups organising this event.
    organiser_contacts : ~django.db.models.query.QuerySet of \
    ~loefsys.users.models.Contact
        A query of all people defined as contact persons for this event.
    event_start : ~datetime.datetime
        The start date and time of the event.
    event_end : ~datetime.datetime
        The end date and time of the event.
    category : ~loefsys.events.models.choices.EventCategories
        The category of the event.
    price : ~decimal.Decimal
        The price.
    location : str
        The location of the event.

        We might want to include a Google Maps widget showing the location.
        `django-google-maps <https://pypi.org/project/django-google-maps/>`_ might be
        useful for this.
    is_open_event : bool
        Flag to determine if non-members can register.
    published : bool
        Flag to determine if the event is publicly visible.
    eventregistration_set : ~loefsys.events.models.managers.EventRegistrationManager
        A manager of registrations for this event.

        It is the one-to-many relationship to
        :class:`~loefsys.events.models.EventRegistration`.
    """

    organiser_groups = models.ManyToManyField(
        to=LoefbijterGroup, related_name="events_organiser", blank=True
    )
    organiser_contacts = models.ManyToManyField(
        to=Contact, related_name="events_contact", blank=True
    )

    event_start = models.DateTimeField(_("start time"))
    event_end = models.DateTimeField(_("end time"))

    category = models.PositiveSmallIntegerField(
        choices=EventCategories, verbose_name=_("category")
    )

    price = models.DecimalField(
        _("price"),
        max_digits=5,
        decimal_places=2,
        default=Decimal("0.00"),
        blank=True,
        validators=[validators.MinValueValidator(0)],
    )
    fine = models.DecimalField(
        _("fine"),
        max_digits=5,
        decimal_places=2,
        default=Decimal("0.00"),
        blank=True,
        help_text=_("Fine if participant does not show up."),
        validators=[validators.MinValueValidator(0)],
    )

    location = models.CharField(_("location"), max_length=255)

    is_open_event = models.BooleanField(
        help_text=_("Event is open for non-members"), default=False
    )

    published = models.BooleanField(_("published"), default=False)

    eventregistration_set: EventRegistrationManager

    objects = EventManager()

    def __str__(self):
        return f"{self.__class__.__name__} {self.title}"

    def registrations_open(self) -> bool:
        """Determine whether it is possible for users to register for this event.

        By default, registration is only open when the event is published and the event
        hasn't ended yet.

        Returns
        -------
        bool
            A boolean that defines whether registrations are open.
        """
        return self.published and timezone.now() < self.event_end

    def max_capacity_reached(self) -> bool:
        """Check whether the max capacity for this event is reached.

        Returns
        -------
        bool
            ``True`` when the event is full and ``False`` if there are places available.
        """
        return False

    def fine_on_cancellation(self) -> bool:
        """Check whether the cancellation of a registration will result in a fine.

        Returns
        -------
        bool
            ``True`` when a fine will be applied and ``False`` when cancellation is
            free of charge.
        """
        return True

    def process_cancellation(self) -> None:
        """Process the side effects for an event of a cancellation.

        Returns
        -------
        None
        """

    @override
    def clean(self) -> None:
        """Clean up model fields.

        Returns
        -------
        None
        """
        super().clean()
        # Custom validation to ensure at least one organizer or contact is set
        if not self.organiser_groups.exists() and not self.organiser_contacts.exists():
            raise ValidationError("At least one organiser or contact should be set.")


class RequiredRegistrationEvent(Event):
    """Model for an event with mandatory registration.

    In this model a Registration is required in order to attend, a good example would
    be a weekend. As there is a clear capacity and a clear cost attached to this event.

    Attributes
    ----------
    registration_start : ~datetime.datetime
        The timestamp at which registrations open.
    registration_end : ~datetime.datetime
        The timestamp at which registrations close.
    cancel_deadline : ~datetime.datetime, None
        The deadline until which registration can be cancelled free of charge.
    """

    registration_start = models.DateTimeField(
        _("registration start"),
        help_text=_(
            "Prefer times when people don't have lectures, "
            "e.g. 12:30 instead of 13:37."
        ),
    )

    registration_end = models.DateTimeField(
        _("registration end"),
        help_text=_(
            "If you set a registration period registration will be "
            "required. If you don't set one, registration won't be "
            "required."
        ),
    )

    cancel_deadline = models.DateTimeField(_("cancel deadline"), null=True, blank=True)

    send_cancel_email = models.BooleanField(
        _("send cancellation notifications"),
        default=True,
        help_text=_(
            "Send an email to the organising party when a member "
            "cancels their registration after the deadline."
        ),
    )

    max_capacity = models.PositiveSmallIntegerField(
        _("maximum number of participants"), blank=True, null=True
    )

    @override
    def registrations_open(self) -> bool:
        """Determine whether it is possible for users to register for this event.

        For events with required registration, registration is only possible when the
        event is published and in the
        registration window defined by :attr:`.registration_start` and
        :attr:`.registration_end`.

        Returns
        -------
        bool
            A boolean that defines whether registrations are open.
        """
        return (
            super().registrations_open()
            and self.registration_start < timezone.now() < self.registration_end
        )

    @override
    def max_capacity_reached(self) -> bool:
        """Determine whether the maximum capacity for the event is reached.

        Returns
        -------
        bool
            ``True`` when the capacity of the event is reached and ``False`` when there
            are places available.
        """
        return (
            self.max_capacity is not None
            and self.max_capacity <= self.eventregistration_set.active().count()
        )

    @override
    def fine_on_cancellation(self) -> bool:
        """Flag to determine if the registration can be cancelled without cost.

        Cancellation is free of charge until the start of the event when no cancellation
        deadline is given, otherwise it must be before the cancellation deadline.

        Returns
        -------
        bool
            ``True`` when the registration can be cancelled without having to pay a
            fine. ``False`` when a fine has to be paid for cancellation.
        """
        deadline: datetime = self.cancel_deadline or self.event_start
        return deadline < timezone.now()

    @override
    def process_cancellation(self) -> None:
        num_active = self.eventregistration_set.active().count()
        num_queued = self.eventregistration_set.queued().count()
        if not num_queued or num_active >= self.max_capacity:
            return

        num_available = self.max_capacity - num_active
        num_to_add = min(num_available, num_queued)
        objs = self.eventregistration_set.queued().order_by_creation()[:num_to_add]
        modified = timezone.now()
        for obj in objs:
            obj.status = RegistrationStatus.ACTIVE
            obj.modified = modified
        self.eventregistration_set.bulk_update(objs, ["status", "modified"])
        # As save() isn't called on the objects, we manually update the field modified.
