"""Module containing the definition for the group membership model."""

import datetime

from django.db import models
from django.utils.translation import gettext_lazy as _
from django_extensions.db.models import TimeStampedModel

from loefsys.users.models import Contact

from .group import Group


class GroupMembership(TimeStampedModel):
    """Describes a group membership.

    It is the link between the many-to-many relationship of
    :class:`~loefsys.groups.models.Group` and :class:`~loefsys.users.models.Contacts`.

    Attributes
    ----------
    created : ~datetime.datetime
        The date and time that this model was created.
    modified : ~datetime.datetime
        The date and time that this model was last modified.
    group : ~loefsys.groups.models.Group
        The group that the membership applies to.
    contact : ~loefsys.users.models.Contacts, None
        The person that the membership applies to. It is set to ``None`` when the user
        is removed for privacy.
    chair : bool
        Defines whether this member has admin privileges for this group.
    role : str
        The role of the member, if applicable.
    member_since : ~datetime.date
        The date that the person became member of the group.
    member_until : ~datetime.date
        The date that the member left/leaves the group.
    note : str
        A potential note on this membership.
        TODO is this needed?
    """

    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name=_("group"))
    contact = models.ForeignKey(Contact, models.SET_NULL, null=True)

    chair = models.BooleanField(verbose_name=_("chair"), default=False)
    role = models.CharField(
        _("role"), help_text=_("The role of this member"), max_length=255, blank=True
    )
    member_since = models.DateField(
        verbose_name=_("member since"),
        help_text=_("The date this member joined in this role"),
        default=datetime.date.today,
    )
    member_until = models.DateField(
        verbose_name=_("member until"),
        help_text=_("A member until this time."),
        blank=True,
        null=True,
    )

    note = models.CharField(max_length=256, blank=True)

    def __str__(self):
        return f"Membership of {self.contact} for {self.group}"
