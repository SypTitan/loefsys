from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core import validators

from phonenumber_field.modelfields import PhoneNumberField
from localflavor.generic.models import IBANField

from utils import countries


class GuestContactDetails(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, models.CASCADE, related_name="guest_form"
    )

    phone_number = PhoneNumberField()

    IBAN = IBANField(
        null=True,
        blank=True,
    )

    address_street = models.CharField(
        max_length=100,
        validators=[
            validators.RegexValidator(
                regex=r"^.+ \d+.*",
                message=_("please use the format <street> <number>"),
            )
        ],
        verbose_name=_("Street and house number"),
        null=True,
        blank=True,
    )

    address_street2 = models.CharField(
        max_length=100,
        verbose_name=_("Second address line"),
        blank=True,
        null=True,
    )

    address_postal_code = models.CharField(
        max_length=10,
        verbose_name=_("Postal code"),
        null=True,
        blank=True,
    )

    address_city = models.CharField(
        max_length=40,
        verbose_name=_("City"),
        null=True,
        blank=True,
    )

    address_country = models.CharField(
        max_length=2,
        choices=countries.EUROPE,
        verbose_name=_("Country"),
        null=True,
        blank=True,
    )
