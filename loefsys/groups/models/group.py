"""Module defining the generic group model."""

from django.db import models
from django.db.models import Case, Q, When
from django.db.models.functions import Now
from django.utils.translation import gettext_lazy as _

from loefsys.groups.models.managers import GroupManager
from loefsys.users.models import Contact


class Group(models.Model):
    """Describes a group of members.

    TODO @Mark expand on this.

    Attributes
    ----------
    name : str
        The name of the group.
    description : str
        A description of the group.
    date_foundation : ~datetime.date
        The date that the group was founded on.
    date_discontinuation : ~datetime.date, None
        The date that the group ceased to exist.
    active : bool
        A flag whether the group is currently active.

        It is a property calculated by whether :attr:`.date_discontinuation` exists and
        whether the date has passed.
    members : ~django.db.models.query.QuerySet of \
    ~loefsys.users.models.Contact
        A query of all members involved in a group.

        It is the many-to-many-relationship to :class:`~loefsys.users.models.Contact`.
    display_members : bool
        A flag that determines whether the members of the group are publicly visible.
    """

    name = models.CharField(max_length=40, verbose_name=_("Groupname"), unique=True)
    description = models.TextField()
    date_foundation = models.DateField(_("Date of foundation"))
    date_discontinuation = models.DateField(_("Date of discontinuation"), null=True)
    active = models.GeneratedField(  # TODO needs testing
        expression=Case(
            When(
                date_discontinuation__isnull=False,
                then=Q(date_discontinuation__gte=Now()),
            ),
            default=True,
        ),
        output_field=models.BooleanField(),
        db_persist=True,
    )
    members = models.ManyToManyField(Contact, related_name="groups_member", blank=True)
    display_members = models.BooleanField(_("Display group members"))

    objects = GroupManager()

    class Meta:
        abstract = True

    def __str__(self):
        return f"Group {self.name}"
