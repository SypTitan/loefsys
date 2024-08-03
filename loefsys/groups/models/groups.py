"""Module defining the various groups that exist within Loefbijter.

All implementations inherit the generic :class:`~loefsys.groups.models.Group` model.
"""

from django.db import models
from django.utils.translation import gettext_lazy as _

from loefsys.groups.models import Group
from loefsys.groups.models.choices import FraternityGenders


class Board(Group):
    """A group model for the board of Loefbijter.

    TODO @Mark expand on this.

    Attributes
    ----------
    year : int
        The year of the board, starting in the founding year.
    """

    year = models.GeneratedField(
        expression=models.F("date_foundation") - 1966,
        output_field=models.IntegerField(),
        db_persist=True,
    )
    # The founding year is 1967, but that is board 1 so counting starts from 1966.


class Committee(Group):
    """Model representing a committee.

    TODo @Mark expand on this

    Attributes
    ----------
    mandatory : bool
        A flag that shows whether the committee is a mandatory committee. If a committee
        is one of the mandatory committees, new members can be assigned to this
        committee to satisfy their committee duty.
    """

    mandatory = models.BooleanField(
        default=False,
        help_text=_(
            "If this is checked new members should be assigned to this committee, any "
            "members that are part of this committee satisfy their committee_duty."
        ),
    )


class Fraternity(Group):
    """Model defining fraternities within the associations.

    TODO @Mark expand on this.

    Attributes
    ----------
    gender_requirement : FraternityGenders
        The type of fraternity.
    """

    gender_requirement = models.PositiveSmallIntegerField(
        choices=FraternityGenders, default=FraternityGenders.MIXED
    )


class YearClub(Group):
    """A year club consists of a group people belonging to the same year.

    TODO @Mark expand on this

    Attributes
    ----------
    year : int
        The year of the year club.
    """

    year = models.GeneratedField(
        expression=models.F("date_foundation") - 1966,
        output_field=models.IntegerField(),
        db_persist=True,
    )
    # The founding year is 1967, but that year counts as 1 so counting starts from 1966.
