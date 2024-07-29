"""In this module, the models for events are defined.

Two types of events exist. Events with mandatory registration are defined by
:class:`.RequiredRegistrationEvent` and events with optional registration are defined by
:class:`.OptionalRegistrationEvent`. Loefbijter currently does not organize any
activities with optional registration, so it is possible that this model gets deleted in
the future.
"""

from abc import abstractmethod
from decimal import Decimal
from typing import TYPE_CHECKING, override

from django.conf import settings
from django.core import validators
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import QuerySet
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from loefsys.groups.models import Group

if TYPE_CHECKING:
    from loefsys.events.models import EventRegistration


class EventCategory(models.IntegerChoices):
    """Categories for an event.

    Events can be filtered based on their category. This enum is used for the
    filtering.
    """

    OTHER = (0, _("Other"))
    """Used when other categories aren't appropriate."""

    ALUMNI = (1, _("Alumni"))
    """Used for events for ex-members of the association."""

    LEISURE = (2, _("Leisure"))
    """Used for entertainment events.

    Examples are 'borrels', parties, game activites, and more.
    """

    ASSOCIATION = (3, _("Association"))
    """Used for events related to the board.

    Examples are general meetings, or the fries table moment.
    """

    SAILING = (4, _("Sailing"))
    """Used for events directly involving sailing."""

    COMPETITION = (5, _("Competition"))
    """Used for events specifically for sailing competetions.

    Examples are NESTOR, regatta's, and more.
    """


class Event(models.Model):
    """Model for an event.

    TODO @Mark expand on this.

    Attributes:
        title (str): The title to display for the event.
        organiser_groups (QuerySet): A query of all groups organising this event.

            It is the many-to-many relationship to
            :class:`~loefsys.groups.models.Group`.
        organiser_contacts (QuerySet): A query of all contacts for this event.

            It is the many-to-many relationship to
            :class:`~loefsys.users.models.Contacts`.
        event_start (datetime): The start date and time of the event.
        event_end (datetime): The end date and time of the event.
        category (EventCategory): The category of the event.
        price (Decimal): The price
        location (str): The location of the event.
        map_location (str): TODO what is this???
        is_open_event (bool): Flag to determine if non-members can register.
        published (bool): Flag to determine if the event is publicly visible.
        eventregistration_set (QuerySet): The one-to-many relationship to
            :class:`~loefsys.events.models.EventRegistration`.
    """

    title = models.CharField(_("title"), max_length=100)

    organiser_groups = models.ManyToManyField(
        to=Group, related_name="event_organisers", blank=True
    )

    organiser_contacts = models.ManyToManyField(
        to=settings.AUTH_USER_MODEL, related_name="event_contact_persons", blank=True
    )

    event_start = models.DateTimeField(_("start time"))

    event_end = models.DateTimeField(_("end time"))

    category = models.PositiveSmallIntegerField(
        max_length=40,
        choices=EventCategory,
        verbose_name=_("category"),
        help_text=_(
            "Alumni: Events organised for alumni, "
            "Leisure: borrels, parties, game activities etc., "
            "Association Affairs: general meetings or "
            "any other board related events, "
            "Sailing: sailing"
            "Competition: NESTOR, Regatta's etc"
            "Other: anything else."
        ),
    )

    price = models.DecimalField(
        _("price"),
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True,
        validators=[validators.MinValueValidator(0)],
    )
    """Ticket price for the event."""

    fine = models.DecimalField(
        _("fine"),
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True,
        help_text=_("Fine if participant does not show up (at least €5)."),
        validators=[validators.MinValueValidator(5)],
    )
    """Absence fine for not attending the event."""

    location = models.CharField(_("location"), max_length=255)

    map_location = models.CharField(
        _("location for minimap"),
        max_length=255,
        help_text=_(
            "Location of Huygens: Heyendaalseweg 135, Nijmegen. "
            "Location of Mercator 1: Toernooiveld 212, Nijmegen. "
            "Use the input 'discord' or 'online' for special placeholders. "
            "Not shown as text!!"
        ),
    )

    is_open_event = models.BooleanField(
        help_text=_("Event is open for non-members"), default=False
    )

    published = models.BooleanField(_("published"), default=False)

    eventregistration_set: QuerySet["EventRegistration"]

    class Meta:  # noqa D106
        abstract = True

    @override
    def __str__(self):
        return f"{self.__class__.__name__} {self.title}"

    def get_queryset_active_registrations(self) -> QuerySet["EventRegistration"]:
        """Queryset with all active registrations.

        Active registration are registrations that are not cancelled. The QuerySet
        provided by this method is ordered by
        :attr:`loefsys.events.models.EventRegistration.date_registration`.

        Returns:
            A :class:`~django.db.models.query.QuerySet` of :class:`.EventRegistration`.
        """
        return self.eventregistration_set.filter(cancelled=False).order_by("date")

    def registrations_open(self) -> bool:
        """Determines whether it is possible for users to register for this event.

        By default, registration is only open when the event is published.

        Returns:
            A boolean that defines whether registrations are open.
        """
        return self.published

    @abstractmethod
    def registration_is_fined(self, registration: "EventRegistration") -> bool:
        """Check to see if a provided registration is fined for cancelling.

        Args:
            registration (EventRegistration): The registration on which the check is
                performed.

        Returns:
            `True` if the registration is fined and `False` if the registration is not
            fined.
        """
        raise NotImplementedError("This method must be overridden by subclasses.")

    @abstractmethod
    def registration_costs(self, registration: "EventRegistration") -> Decimal:
        raise NotImplementedError("This method must be overridden by subclasses.")

    @override
    def clean(self):
        super().clean()
        # Custom validation to ensure at least one organizer or contact is set
        if not self.organiser_groups.exists() and not self.organiser_contacts.exists():
            raise ValidationError("At least one organiser or contact should be set.")


class RequiredRegistrationEvent(Event):
    """Model for an event with mandatory registration.

    TODO @Mark expand on this.

    Attributes:
        registration_start (datetime): The timestamp at which registrations open.
        registration_end (datetime): The timestamp at which registrations close.
        cancel_deadline (datetime | None): The timestamp until which registrations can
            be cancelled free of charge.
        send_cancel_email (bool): A flag that determines whether the user gets an email
            upon cancellation.
        max_participants (int | None): The max amount of participants for this event.
    """

    registration_start = models.DateTimeField(
        _("registration start"),
        help_text=_(
            "Prefer times when people don't have lectures, "
            "e.g. 12:30 instead of 13:37."
        ),
    )
    """The date and time at which registrations for this event open."""

    registration_end = models.DateTimeField(
        _("registration end"),
        help_text=_(
            "If you set a registration period registration will be "
            "required. If you don't set one, registration won't be "
            "required."
        ),
    )
    """The date and time at which registrations for this event closes."""

    cancel_deadline = models.DateTimeField(_("cancel deadline"), null=True, blank=True)
    """The date and time for the cancellation deadline.

    People who have a registration for this event are able to cancel before expiration
    of this date and time.
    """

    send_cancel_email = models.BooleanField(
        _("send cancellation notifications"),
        default=True,
        help_text=_(
            "Send an email to the organising party when a member "
            "cancels their registration after the deadline."
        ),
    )
    """Flag to determine whether people receive an email for cancelling for this event.
    """

    max_participants = models.PositiveSmallIntegerField(
        _("maximum number of participants"), blank=True, null=True
    )
    """The maximum number of participants allowed to register for this event."""

    @override
    def registration_is_fined(self, registration: "EventRegistration") -> bool:
        """Check to see if a provided registration is fined for cancelling.

        For an event with required registration, a fine only applies when a cancellation
        deadline exists and the cancellation of the registration occurred after this
        deadline.

        Args:
            registration (EventRegistration): The registration on which the check is
                performed.

        Returns:
            `True` if the registration is fined and `False` if the registration is not
            fined.
        """
        if self.cancel_deadline and registration.date_cancellation:
            return self.cancel_deadline < registration.date_cancellation
        return False

    @override
    def registration_costs(self, registration: "EventRegistration") -> Decimal:
        return self.fine if self.registration_is_fined(registration) else self.price

    def participants(self) -> QuerySet["EventRegistration"]:
        """Return the active participants."""
        if self.max_participants is None:
            return self.get_queryset_active_registrations()
        return self.get_queryset_active_registrations()[: self.max_participants]

    def queue(self) -> QuerySet["EventRegistration"]:
        """Return the waiting queue."""
        if self.max_participants is None:
            return self.get_queryset_active_registrations().none()
        return self.get_queryset_active_registrations()[self.max_participants :]

    def reached_participants_limit(self) -> bool:
        """Determine whether the maximum capacity for the event is reached."""
        return (
            self.max_participants is not None
            and self.max_participants
            <= self.get_queryset_active_registrations().count()
        )

    def can_cancel_for_free(self) -> bool:
        """Flag to determine if the registration can be cancelled without cost."""
        if self.cancel_deadline:
            return timezone.now() < self.cancel_deadline
        return True

    @override
    def registrations_open(self) -> bool:
        """Determines whether it is possible for users to register for this event.

        For events with required registration, registration is only possible when the
        event is published and in the
        registration window defined by :attr:`.registration_start` and
        :attr:`.registration_end`.

        Returns:
            A boolean that defines whether registrations are open.
        """
        return (
            super().registrations_open()
            and self.registration_start < timezone.now() < self.registration_end
        )


class OptionalRegistrationEvent(Event):
    """Model for an event with optional registration.

    TODO @Mark expand on this.
    """

    @override
    def registrations_open(self) -> bool:
        """Determines whether it is possible for users to register for this event.

        For an event with optional registration, registrations are open when the event
        is published as long as the event hasn't ended yet.

        Returns:
            A boolean that defines whether registrations are open.
        """
        return super().registrations_open() and timezone.now() < self.event_end

    @override
    def registration_is_fined(self, registration: "EventRegistration") -> bool:
        """Check to see if a provided registration is fined for cancelling.

        For events with optional registration, no fine exists.

        Args:
            registration (EventRegistration): The registration on which the check is
                performed.

        Returns:
            ``True`` if the registration is fined and ``False`` if the registration is
            not fined. For an event with optional registration, this is permanently
            ``False``.
        """
        return False

    @override
    def registration_costs(self, registration: "EventRegistration") -> Decimal:
        return Decimal("0.00")
