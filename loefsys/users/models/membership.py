import datetime

from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from loefsys.utils.snippets import overlaps
from loefsys.users.models import Person


class MembershipTypes(models.TextChoices):
    ACTIVE = "ACT", _("Active member")
    PASSIVE = "PAS", _("Passive member")
    ALUMNUS = "ALM", _("Alumnus")


class Membership(models.Model):
    person = models.ForeignKey(
        to=Person,
        on_delete=models.CASCADE,
        verbose_name=_("User"),
    )

    membership_type = models.CharField(
        max_length=3,
        choices=MembershipTypes.choices,
        default=MembershipTypes.ACTIVE,
        verbose_name=_("Membership type"),
    )

    since = models.DateField(
        verbose_name=_("Membership since"),
        help_text=_("The date the member's membership started"),
        default=datetime.date.today,
    )

    until = models.DateField(
        verbose_name=_("Membership until"),
        help_text=_("The date the member's membership stopped"),
        null=True,
        blank=True,
    )

    def clean(self):
        super().clean()

        errors = {}
        if self.until and (not self.since or self.until < self.since):
            raise ValidationError({"until": _("End date can't be before start date")})

        if self.since is not None:
            memberships = self.person.membership_set.all()
            if overlaps(self, memberships):
                errors.update(
                    {
                        "since": _("A membership already exists for that period"),
                        "until": _("A membership already exists for that period"),
                    }
                )

        if errors:
            raise ValidationError(errors)

    def is_active(self):
        today = timezone.now().date()
        return self.since <= today and (not self.until or self.until > today)

    def __str__(self):
        return super().__str__()  # TODO improve
