from typing import TYPE_CHECKING

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.db.models import QuerySet
from django.utils.translation import gettext_lazy as _

from loefsys.users.managers import UserManager

if TYPE_CHECKING:
    from .membership import Membership


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    # Continue using email as username or also move to contacts?

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    membership_set: QuerySet["Membership"]

    def __str__(self):
        return self.email
