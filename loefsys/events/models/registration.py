from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from loefsys.users.models.contact import Contact

from .event import Event


class EventRegistration(models.Model):
    """Registration model for an event.

    TODO @Mark expand on this.

    Attributes:
        event (Event): The event to which the registration applies.
        contact (Contact): The contact that the registration is for.
        event_price (Decimal): The price of the event at the time of registration.
        event_fine (Decimal): The fine for cancellation at the time of registration.
        date_registration (datetime): The timestamp of the registration.
        date_cancellation (datetime): The timestamp of the cancellation, if present.
        paid (bool): Flag to determine whether the registration has been paid for.
    """

    event = models.ForeignKey(Event, models.CASCADE)
    contact = models.ForeignKey(Contact, models.SET_NULL, null=True)

    event_price = models.DecimalField(
        _("price"), max_digits=5, decimal_places=2, null=True, blank=True
    )
    event_fine = models.DecimalField(
        _("fine"), max_digits=5, decimal_places=2, null=True, blank=True
    )

    date_registration = models.DateTimeField(
        _("registration date"), default=timezone.now
    )
    date_cancellation = models.DateTimeField(
        _("cancellation date"), null=True, blank=True
    )
    paid = models.BooleanField(default=False)

    class Meta:  # noqa D106
        unique_together = ("event", "user")

    def __str__(self):
        return f"{self.event} | {self.contact}"

    def save(self, *args, **kwargs):
        if self.event_price is None:
            self.event_price = self.event.price
        if self.event_fine is None:
            self.event_fine = self.event.fine
        super().save(*args, **kwargs)

    @property
    def cancelled(self) -> bool:
        return self.date_cancellation is not None

    # TODO: Change to agreed price
    @property
    def costs(self):
        return self.event.registration_costs(self)
