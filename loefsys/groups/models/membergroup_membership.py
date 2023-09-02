import datetime

from django.db import models

from django.utils.translation import gettext_lazy as _

from django.conf import settings

from .membergroup import MemberGroup


class ActiveMembershipManager(models.Manager):
    """Custom manager that gets the currently active membergroup memberships."""

    def get_queryset(self):
        return super().get_queryset().exclude(group__active=False).order_by("group__name")


class MemberGroupMembership(models.Model):
    """Describes a group membership."""

    objects = models.Manager()
    active_objects = ActiveMembershipManager()

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        models.SET_NULL,
        null=True
        # limit_choices_to=registration_user_choices_limit,
    )

    group = models.ForeignKey(
        MemberGroup,
        on_delete=models.CASCADE,
        verbose_name=_("Group"),
    )

    chair = models.BooleanField(
        verbose_name=_("Chair of the group"),
        default=False,
    )

    role = models.CharField(
        _("role"),
        help_text=_("The role of this member"),
        max_length=255,
        blank=True,
        null=True,
    )

    since = models.DateField(
        verbose_name=_("Member since"),
        help_text=_("The date this member joined in this role"),
        default=datetime.date.today,
    )

    until = models.DateField(
        verbose_name=_("Member until"),
        help_text=_("A member until this time (can't be in the future)."),
        blank=True,
        null=True,
    )

    note = models.CharField(
        max_length=256,
        blank=True,
    )
