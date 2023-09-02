from django.db import models

from django.contrib.auth.models import User
from django.conf import settings


class Committee(models.Model):
    name = models.CharField(
        max_length=20,
    )

    members = models.ManyToManyField(
        to=settings.AUTH_USER_MODEL,
        through="committees.CommitteeMembership",
        through_fields=("committee", "user"),
        symmetrical=True,
        blank=True,
    )

    @property
    def active_memberships(self):
        return self.committeemembership_set.filter(is_active=True)

    @property
    def head(self):
        return self.active_memberships.filter(is_head=True).user

    def __str__(self):
        return self.name
