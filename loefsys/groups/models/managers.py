"""Module containing the custom managers for the models in the groups app."""

from typing import TYPE_CHECKING

from django.db import models
from django.db.models import QuerySet
from django.db.models.functions import Now

if TYPE_CHECKING:
    from .group import Group
    from .membership import GroupMembership


class GroupManager[TGroup: "Group"](models.Manager[TGroup]):
    """Custom manager for group models.

    The manager is used by models inheriting the :class:`~loefsys.groups.models.Group`
    model.
    """

    def active(self) -> QuerySet[TGroup]:
        """Filter and return only groups that are active.

        Returns
        -------
        ~django.db.models.query.QuerySet of ~loefsys.groups.models.Group
            A query of filtered :class:`~loefsys.groups.models.Group` implementations.
        """
        return self.filter(active=True)


class GroupMembershipManager(models.Manager["GroupMembership"]):
    """Custom manager for the :class:`~loefsys.groups.models.Group` model."""

    def active(self) -> QuerySet["GroupMembership"]:
        """Filter and return only active group memberships.

        Returns
        -------
        ~django.db.models.query.QuerySet of ~loefsys.groups.models.GroupMembership
            A query of filtered memberships that are active.
        """
        return self.filter(member_until__lte=Now())
