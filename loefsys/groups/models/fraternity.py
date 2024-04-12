import datetime

from django.db import models

from .group import Group


class Fraternity(Group):
    GENDER_CHOICES = (
        ("MIXED", "Mixed"),
        ("FEMALE", "Female"),
        ("MALE", "Male"),
    )

    gender_requirement = models.CharField(
        max_length=6,
        choices=GENDER_CHOICES,
        default="MIXED",
    )

