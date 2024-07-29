"""Module containing the model for an event registration."""

from decimal import Decimal

from django.db import models
from django.db.models import Case, When
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from loefsys.users.models import Contacts

from .event import Event


class EventRegistration(models.Model):
    """Registration model for an event.

    TODO @Mark expand on this.

    Attributes:
        event (Event): The event to which the registration applies.
        contact (Contact): The contact that the registration is for.
        paid (bool): Flag to determine whether the registration has been paid for.
        event_price (Decimal): The price of the event at the time of registration.
        event_fine (Decimal): The fine for cancellation at the time of registration.
        date_registration (datetime): The timestamp of the registration.
        date_cancellation (datetime): The timestamp of the cancellation, if present.
        cancelled (bool): Flag to determine whether the registration is cancelled.
    """

    event = models.ForeignKey(Event, models.CASCADE)
    contact = models.ForeignKey(Contacts, models.SET_NULL, null=True)

    paid = models.BooleanField(default=False)
    event_price = models.DecimalField(
        _("price"), max_digits=5, decimal_places=2, blank=True
    )
    event_fine = models.DecimalField(
        _("fine"), max_digits=5, decimal_places=2, blank=True
    )

    date_registration = models.DateTimeField(
        _("registration date"), default=timezone.now
    )
    date_cancellation = models.DateTimeField(
        _("cancellation date"), null=True, blank=True
    )
    cancelled = models.GeneratedField(  # TODO needs testing
        expression=Case(When(date_cancellation__isnull=True, then=False), default=True),
        output_field=models.BooleanField(),
        db_persist=True,
    )

    class Meta:  # noqa D106
        unique_together = ("event", "user")

    def __str__(self):
        return f"{self.event} | {self.contact}"

    def save(self, **kwargs):
        """Saves the model to the database.

        When creating a new registration, the attributes :attr:`.event_price` and
        :attr:`.event_fine` are copied from the :attr`.event`.
        """
        if self._state.adding:
            self.event_price = self.event.price
            self.event_fine = self.event.fine
        super().save(**kwargs)

    @property
    def costs(self) -> Decimal:
        """The price to pay for this event."""
        return (
            self.event_fine
            if self.event.registration_is_fined(self)
            else self.event_price
        )
