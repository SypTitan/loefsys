from django.core import validators
from django.db import models
from django.utils.translation import gettext_lazy as _


class ReservableType(models.Model):
    """Describes a type of material that can be reserved."""

    class Reservables(models.IntegerChoices):
        BOAT = 1, _("Boat")
        ROOM = 2, _("Room")
        MATERIAL = 3, _("Material")

    type_of_reservable = models.SmallIntegerField(
        verbose_name=("Reservable Type"),
        choices=Reservables.choices,
    )

    name = models.CharField(
        max_length=40,
        verbose_name=("Material Type"),
        unique=True,
    )

    description = models.TextField()

    def __str__(self):
        return self.name


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

    reservable_type = models.ForeignKey(
        "ReservableType",
        on_delete=models.SET_DEFAULT,
        default=None,
        null=True,
        blank=True,
        related_name="materials",
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

    external_price = models.DecimalField(
        _("price for externals"),
        max_digits=5,
        decimal_places=2,
        default=0,
        validators=[validators.MinValueValidator(0)],
    )

    def __str__(self):
        return super().__str__()  # TODO improve
