import datetime

from django.db import models

from .membergroup import MemberGroup


class YearClub(MemberGroup):
    year = models.IntegerField(default=datetime.date.today().year - 1967)
