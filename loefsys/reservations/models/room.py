from django.db import models
from .reservable import Reservable


class Room(Reservable):

    name = models.CharField(max_length=40, verbose_name=("Roomname"), unique=True)

    capacity = models.IntegerField()



