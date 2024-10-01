"""Module defining the user account model for the website."""

from typing import TYPE_CHECKING

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db.models import EmailField
from django_extensions.db.models import TimeStampedModel

if TYPE_CHECKING:
    from .contact import Contact


class User(AbstractBaseUser, PermissionsMixin, TimeStampedModel):
    """The user model for authentication on the Loefbijter website.

    Attributes
    ----------
    created : ~datetime.datetime
        The timestamp of the creation of this model.
    modified : ~datetime.datetime
        The timestamp of last modification of this model.
    email : str
        The email used for the account to log in.
    password : str
        The password for this user.
    last_login : ~datetime.datetime
        the timestamp of the last login for this user.
    is_superuser : bool
        Designated that this user has all permissions without explicit assignation.
    groups : ~django.contrib.auth.models.Group
        The groups that this user belongs to.
    user_permissions : ~django.contrib.auth.models.Permission
        The specific permissions for this user.
    """

    email = EmailField(unique=True)

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ("email",)

    contact: "Contact"

    def __str__(self):
        return f"User {self.email}"
