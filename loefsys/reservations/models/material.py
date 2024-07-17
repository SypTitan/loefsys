from django.db import models

from .reservable import Reservable


class Material(Reservable):
    """Describes a material that can be reserved."""

    size = models.CharField(max_length=10)

    quantity = models.PositiveIntegerField(default=1)
