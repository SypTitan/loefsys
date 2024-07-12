from django.db import models

from .reservable import Reservable


class ComplicationLog(models.Model):
    reservable = models.ForeignKey(Reservable, on_delete=models.CASCADE)

    log = models.TextField()

    def __str__(self):
        return super().__str__()  # TODO improve
