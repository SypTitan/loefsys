"""Module defining the user account model for the website."""

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.db.models import OneToOneField
from django_extensions.db.models import TimeStampedModel

from loefsys.contacts.models.contact import Contact


class User(AbstractBaseUser, PermissionsMixin, TimeStampedModel):
    """The user model for authentication on the Loefbijter website.

    Attributes
    ----------
    created : ~datetime.datetime
        The timestamp of the creation of this model.
    modified : ~datetime.datetime
        The timestamp of last modification of this model.
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
    contact : ~loefsys.contacts.models.contact.Contact
        The contact that the user account is connected to.
    """

    # Using a trick here, by setting to_field="email", the email string is automatically
    # used as username when logging in.
    contact = OneToOneField(to=Contact, to_field="email", on_delete=models.CASCADE)

    USERNAME_FIELD = "contact"

    def __str__(self):
        return f"User {self.contact.email}"
