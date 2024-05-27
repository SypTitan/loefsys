import datetime

from django.db import models

from .group import Group


class YearClub(Group):
    year = models.IntegerField(default=datetime.date.today().year - 1967)
