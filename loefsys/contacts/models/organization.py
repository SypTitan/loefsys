"""Module containing the definition for an organization."""

from django.db import models
from django.utils.translation import gettext_lazy as _
from django_extensions.db.models import TimeStampedModel

from loefsys.contacts.models.contact import Contact


class Organization(TimeStampedModel):
    """Model of a contact representing an organization.

    Attributes
    ----------
    created : ~datetime.datetime
        The timestamp of the creation of this model.
    modified : ~datetime.datetime
        The timestamp of last modification of this model.
    contact : ~loefsys.contacts.models.contact.Contact
        The contact information that the organizational details belong to.
    name : str
        The organization's name.
    website : str
        The organization's website.
    """

    contact = models.OneToOneField(
        to=Contact, on_delete=models.CASCADE, related_name="organization"
    )
    name = models.CharField(max_length=100, verbose_name=_("Organisation name"))
    website = models.URLField(verbose_name=_("Website"), blank=True)

    def __str__(self):
        return f"Organization {self.name}"
