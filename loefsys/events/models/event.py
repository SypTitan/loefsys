from django.core import validators
from django.db import models
from django.urls import reverse
from django.utils import timezone

from django.utils.translation import gettext_lazy as _
from django.utils.text import format_lazy


class Event(models.Model):
    CATEGORY_ALUMNI = "alumni"
    CATEGORY_LEISURE = "leisure"
    CATEGORY_ASSOCIATION = "association"
    CATEGORY_SAILING = "sailing"
    CATEGORY_COMPETITION = "competition"
    CATEGORY_OTHER = "other"

    EVENT_CATEGORIES = (
        (CATEGORY_ALUMNI, _("Alumni")),
        (CATEGORY_LEISURE, _("Leisure")),
        (CATEGORY_ASSOCIATION, _("Association Affairs")),
        (CATEGORY_SAILING, _("Sailing")),
        (CATEGORY_COMPETITION, _("Competition")),
        (CATEGORY_OTHER, _("Other")),
    )

    DEFAULT_NO_REGISTRATION_MESSAGE = _("No registration required")

    title = models.CharField(_("title"), max_length=100)

    # description = HTMLField(_("description"),)

    # organiser (should use contenttypes for user, committee, yearclub)

    is_open_event = models.BooleanField(
        help_text=_("Event is open for non-members"),
        default=False,
    )

    start = models.DateTimeField(_("start time"))

    end = models.DateTimeField(_("end time"))

    category = models.CharField(
        max_length=40,
        choices=EVENT_CATEGORIES,
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

    registration_start = models.DateTimeField(
        _("registration start"),
        null=True,
        blank=True,
        help_text=_(
            "If you set a registration period registration will be "
            "required. If you don't set one, registration won't be "
            "required. Prefer times when people don't have lectures, "
            "e.g. 12:30 instead of 13:37."
        ),
    )

    registration_end = models.DateTimeField(
        _("registration end"),
        null=True,
        blank=True,
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

    optional_registrations = models.BooleanField(
        _("allow optional registrations"),
        default=True,
        help_text=_(
            "Participants can indicate their optional presence, even though "
            "registration is not actually required. This ignores registration "
            "start and end time or cancellation deadlines, optional "
            "registration will be enabled directly after publishing until the "
            "end of the event."
        ),
    )

    location = models.CharField(
        _("location"),
        max_length=255,
    )

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

    price = models.DecimalField(
        _("price"),
        max_digits=5,
        decimal_places=2,
        default=0,
        validators=[validators.MinValueValidator(0)],
    )

    fine = models.DecimalField(
        _("fine"),
        max_digits=5,
        decimal_places=2,
        default=0,
        # Minimum fine is checked in this model's clean(), as it is only for
        # events that require registration.
        help_text=_("Fine if participant does not show up (at least €5)."),
        validators=[validators.MinValueValidator(0)],
    )

    max_participants = models.PositiveSmallIntegerField(
        _("maximum number of participants"),
        blank=True,
        null=True,
    )

    no_registration_message = models.CharField(
        _("message when there is no registration"),
        max_length=200,
        blank=True,
        default=DEFAULT_NO_REGISTRATION_MESSAGE,
        help_text=(
            format_lazy("{} {}", _("Default:"), DEFAULT_NO_REGISTRATION_MESSAGE)
        ),
    )

    published = models.BooleanField(_("published"), default=False)

    @property
    def active_registrations(self):
        """Queryset with all non-cancelled registrations."""
        return self.eventregistration_set.filter(date_cancelled=None)

    @property
    def participants(self):
        """Return the active participants."""
        if self.max_participants is not None:
            return self.active_registrations.order_by("date")[: self.max_participants]
        return self.active_registrations.order_by("date")

    @property
    def queue(self):
        """Return the waiting queue."""
        if self.max_participants is not None:
            return self.active_registrations.order_by("date")[self.max_participants :]
        return []

    @property
    def registration_required(self):
        return self.registration_start and self.registration_end

    @property
    def can_cancel_for_free(self):
        return self.registration_required and (self.cancel_deadline > timezone.now())

    @property
    def reached_participants_limit(self):
        """Is this event up to capacity?."""
        return (
            self.max_participants is not None
            and self.max_participants <= self.active_registrations.count()
        )

    @property
    def registration_closed(self):
        return (
            self.registration_end is not None and timezone.now() > self.registration_end
        )

    def get_absolute_url(self):
        return reverse("events:event", args=[str(self.pk)])

    def __str__(self):
        return self.title
