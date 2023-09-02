from django.db import models
from django.conf import settings

from ..reservation_log import Log


class Reservation(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=False,
    )

    log_entry = models.ForeignKey(
        Log,
        on_delete=models.CASCADE
    )

    # can be linked to group or event

    @property
    def cost(self):
        return 0
