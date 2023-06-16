from django.db import models


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
