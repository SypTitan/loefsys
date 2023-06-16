from django.db import models

from ..reservable import Room
from .reservation import Reservation


class RoomReservation(Reservation):

    room = models.ForeignKey(
        Room,
        on_delete=models.CASCADE
    )
