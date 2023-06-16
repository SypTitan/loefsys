from django.db import models
from .reservable import Reservable


class ComplicationLog(models.Model):
    reservable = models.ForeignKey(
        Reservable,
        on_delete=models.CASCADE
    )

    log = models.TextField()
