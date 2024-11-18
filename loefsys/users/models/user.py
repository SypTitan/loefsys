"""Module defining the user account model for the website."""

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_extensions.db.models import TimeStampedModel
from phonenumber_field.modelfields import PhoneNumberField

from loefsys.groups.models import LoefbijterGroup
from loefsys.users.models.name_mixin import NameMixin


class User(AbstractBaseUser, PermissionsMixin, NameMixin, TimeStampedModel):
    """The user model for authentication on the Loefbijter website.

    A user account can be made for two use cases. First, when a member registers at
    Loefbijter, an account is made for them as it is necessary for them to interact with
    loefsys for their membership. Additionally, it is also possible that a user account
    is made for guests who need access to the site. This user model is used for both
    cases and the only difference in model values is that a member has a

    Attributes
    ----------
    created : ~datetime.datetime
        The timestamp of the creation of this model.
    modified : ~datetime.datetime
        The timestamp of last modification of this model.
    email : str
        The email of the user, required to log in.
    password : str
        The password for this user.
    last_login : ~datetime.datetime
        the timestamp of the last login for this user.
    is_superuser : bool
        Designated that this user has all permissions without explicit assignation.
    groups : ~django.db.models.query.QuerySet of ~loefsys.groups.models.LoefbijterGroup
        The groups that this user belongs to.
    user_permissions : ~django.db.models.query.QuerySet of \
        ~django.contrib.auth.models.Permission
        The specific permissions for this user.
    phone_number : str
        The phone number of the user.

        For members, a phone number is required, and it is recommended for guest
        accounts too. However, it is possible that no phone number is available for
        ex-members, so the field should take into account empty values too.
    note : str
        A note field that are only visible to active board members.

        For guest accounts, a note can provide information for which purpose this
        account exists. For members, incidents can potentially be tracked.
    """

    email = models.EmailField(unique=True)

    # Copied from PermissionsMixin to override Group type to LoefbijterGroup.
    groups = models.ManyToManyField(
        LoefbijterGroup,
        verbose_name=_("groups"),
        blank=True,
        help_text=_(
            "The groups this user belongs to. A user will get all permissions "
            "granted to each of their groups."
        ),
        related_name="user_set",
        related_query_name="user",
    )

    phone_number = PhoneNumberField(blank=True)
    note = models.TextField(blank=True)

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"

    def __str__(self):
        return f"User {self.email}"
