from django.db import models
from .reservable import Reservable


class Boat(Reservable):

    name = models.CharField(max_length=40, verbose_name=("Boatname"), unique=True)

    boat_type = models.CharField(max_length=32)

    person_capacity = models.IntegerField(default=2)

    has_engine = models.BooleanField(default=False)

    FLEET_CHOICES = (
        ("LOEFBIJTER", "Loefbijter"),
        ("CEULEMANS", "Ceulemans"),
        ("OTHER", "Other"),
    )

    fleet = models.CharField(
        max_length=10,
        choices=FLEET_CHOICES,
        default="LOEFBIJTER",
    )

