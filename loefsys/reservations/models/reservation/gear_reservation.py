from django.db import models

from ..reservable import Gear
from .reservation import Reservation


class GearReservation(Reservation):
    gear = models.ForeignKey(
        Gear,
        on_delete=models.CASCADE,
    )
