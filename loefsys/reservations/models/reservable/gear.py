from django.db import models
from .reservable import Reservable


class Gear(Reservable):

    size = models.CharField(max_length=10)

    type = models.CharField(max_length=32)
