from django.db import models
from django.conf import settings

from ..reservable import Boat
from .reservation import Reservation


class BoatReservation(Reservation):

    boat = models.ForeignKey(
        Boat,
        on_delete=models.CASCADE
    )

    engine_usage = models.DurationField()

    skipper = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        models.SET_NULL,
        null=True
    )





