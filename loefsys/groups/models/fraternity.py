"""Module containing the model definitions for a fraternity."""

from django.db import models

from loefsys.groups.models import LoefbijterGroup
from loefsys.groups.models.choices import FraternityGenders


class Fraternity(LoefbijterGroup):
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
