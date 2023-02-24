from django.db import models

from django.contrib.auth.models import User
from django.utils import timezone


class CommitteeMembership(models.Model):
    user = models.ForeignKey(
        User,
        models.CASCADE,
    )

    committee = models.ForeignKey(
        "committees.Committee",
        models.CASCADE,
    )

    is_head = models.BooleanField(
        default=False,
    )

    since = models.DateField()

    until = models.DateField(
        null=True,
        blank=True,
    )

    note = models.CharField(
        max_length=256,
        blank=True,
    )

    @property
    def is_active(self):
        return self.until is None or self.since > timezone.now() > self.until

    def __str__(self):
        return str(self.committee) + " | " + str(self.user)
