from django.conf import settings
from django.db import models
from django.db.models import Q
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .event import Event


def registration_user_choices_limit(event):
    """Define queryset filters to only include current members."""
    return Q(member__member_until__gt=timezone.now().date())


class EventRegistration(models.Model):
    event = models.ForeignKey(Event, models.CASCADE)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        models.SET_NULL,
        null=True,
        # limit_choices_to=registration_user_choices_limit,
    )

    class Meta:
        unique_together = ("event", "user")

    # if not user.member:
    guest_form = models.ForeignKey(
        "events.GuestContactDetails",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    date = models.DateTimeField(_("registration date"), default=timezone.now)
    date_cancelled = models.DateTimeField(_("cancellation date"), null=True, blank=True)

    present = models.BooleanField(
        _("present"),
        default=False,
    )
    paid = models.BooleanField(
        default=False,
    )

    @property
    def fine(self):
        if self.date_cancelled and self.event.cancel_deadline:
            return self.date_cancelled > self.event.cancel_deadline
        return not self.present

    # TODO: Change to agreed price
    @property
    def costs(self):
        if self.fine:
            return self.event.fine
        return self.event.price

    @property
    def contact(self):
        # TODO create contact JSON from member if user.member, and self.guest_form otherwise.
        return None

    # TODO broken function
    # def __str__(self):
    #    return self.user.get_full_name() if self.user else "Unknown user" + " | " + str(self.event)

    def __str__(self):
        return super().__str__()  # TODO implement later
