"""Module defining the model for a contact."""

from typing import TYPE_CHECKING, Optional

from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_extensions.db.models import TimeStampedModel
from phonenumber_field.modelfields import PhoneNumberField

if TYPE_CHECKING:
    from loefsys.users.models import User

    from .address import Address
    from .organization import Organization
    from .person import Person


class Contact(TimeStampedModel):
    """The model for defining contact information.

    The contact is the base model for a relation, whether that is with a person or an
    organization. It provides all basic required information, such as an email-address,
    to unique identify these contacts.

    In order for a contact to be valid, either a `Person` instance or `Organization`
    instance must link to it. It cannot be valid that a contact has both a `Person` and
    an `Organization` linked to it.

    TODO write logic for Organization and Person that deletion also deletes Contact
        instance. This can possibly be done via signals, but maybe also via an
        ObjectManager. At least it must also take into account bulk deletion, which is
        usually done directly in SQL.

    TODO write test for aforementioned logic.

    Attributes
    ----------
    created : ~datetime.datetime
        The timestamp of the creation of this model.
    modified : ~datetime.datetime
        The timestamp of last modification of this model.
    email : str
        The email for this contact. This field must be unique.
    receive_newsletter : bool
        A flag that determines whether this contact wants to receive the newsletter.
    phone_number : str or None
        The phone number of this contact.
    note : str
        An optional note about this user.
    address : ~loefsys.contacts.models.address.Address or None
        The address of this contact.
    organization : ~loefsys.contacts.models.organization.Organization or None
        The organization that the contact details are for.

        Its assignment is mutually exclusive with the assignment for `person`.
    person : ~loefsys.contacts.models.person.Person or None
        The person that the contact details are for.

        Its assignment is mutually exclusive with the assignment for `organization`.
    user : ~loefsys.users.models.user.User or None
        The user account associated with this contact.

        The object only exists if a user account was made for this contact.
    """

    email = models.EmailField(_("email address"), unique=True)
    receive_newsletter = models.BooleanField(
        verbose_name=_("Receive newsletter"),
        help_text=_("Receive the Newsletter"),
        default=True,
    )  # TODO if we only send newsletter to members, move this field to member model
    phone_number = PhoneNumberField(null=True, blank=True, unique=True)
    note = models.TextField(max_length=500, blank=True)

    address: Optional["Address"]
    organization: Optional["Organization"]
    person: Optional["Person"]
    user: Optional["User"]

    def __str__(self):
        return f"Contact {self.email}"

    def clean(self) -> None:
        """Validate a contact's model fields.

        A Contact instance has either an organization or a person specified. If none or
        both are specified, a ValidationError will be raised.

        Returns
        -------
            None
        """
        if not hasattr(self, "organization") and not hasattr(self, "person"):
            raise ValidationError(
                {
                    "organization": _("Either a person or an organization is required"),
                    "person": _("Either a person or an organization is required"),
                }
            )
        if hasattr(self, "organization") and hasattr(self, "person"):
            raise ValidationError(
                {
                    "organization": _("organization and person can't both be defined"),
                    "person": _("organization and person can't both be defined"),
                }
            )
