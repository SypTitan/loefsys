from django.core import validators
from django.db import models
from .reservable import Reservable

from django.utils.translation import gettext_lazy as _


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

    member_price = models.DecimalField(
        _("price for members"),
        max_digits=5,
        decimal_places=2,
        default=0,
        validators=[validators.MinValueValidator(0)],
    )

    alumni_price = models.DecimalField(
        _("price for alumni"),
        max_digits=5,
        decimal_places=2,
        default=0,
        validators=[validators.MinValueValidator(0)],
    )

    # external_price = models.DecimalField(
    #     _("price for externals"),
    #     max_digits=5,
    #     decimal_places=2,
    #     default=0,
    #     validators=[validators.MinValueValidator(0)],
    # )