from django.core import validators
from django.db import models

from django.utils.translation import gettext_lazy as _


class Reservable(models.Model):
    LOCATION_CHOICES = (
        ("BOARDROOM", "Boardroom"),
        ("BASTION", "Bastion"),
        ("KRAAIJ", "Kraaij"),
    )

    location = models.CharField(
        max_length=10,
        choices=LOCATION_CHOICES,
        default="KRAAIJ",
    )

    reservable = models.BooleanField(
        default=False,
        help_text=(
            "This should only be unchecked if object is currently unreservable."
        ),
    )

    description = models.TextField()

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

    # Quantity?