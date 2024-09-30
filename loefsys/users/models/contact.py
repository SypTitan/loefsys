from django.core import validators
from django.db import models
from django.utils.translation import gettext_lazy as _
from localflavor.generic.models import IBANField
from phonenumber_field.modelfields import PhoneNumberField

from loefsys.utils import countries


class PaymentMethods(models.TextChoices):
    COLLECTION = "IN", _("Collection")


class Genders(models.TextChoices):
    MALE = "M", _("Male")
    FEMALE = "F", _("Female")
    OTHER = "O", _("Other")
    UNSPECIFIED = "U", _("Prefer not to say")


class Contact(models.Model):
    email = models.EmailField(_("email address"), unique=True)

    phone_number = PhoneNumberField()

    remark = models.TextField(max_length=500, blank=True)

    # --- Communication preference ----

    receive_newsletter = models.BooleanField(
        verbose_name=_("Receive newsletter"),
        help_text=_("Receive the Newsletter"),
        default=True,
    )

    # ---- Address information -----

    address_street = models.CharField(
        max_length=100,
        validators=[
            validators.RegexValidator(
                regex=r"^.+ \d+.*", message=_("please use the format <street> <number>")
            )
        ],
        verbose_name=_("Street and house number"),
    )

    address_street2 = models.CharField(
        max_length=100, verbose_name=_("Second address line"), blank=True
    )

    address_postal_code = models.CharField(max_length=10, verbose_name=_("Postal code"))

    address_city = models.CharField(max_length=40, verbose_name=_("City"))

    address_country = models.CharField(
        max_length=2, choices=countries.EUROPE, verbose_name=_("Country")
    )

    def __str__(self):
        return f"Contact information for {self.email}"


class Person(Contact):
    first_name = models.CharField(
        max_length=64, verbose_name=_("First name"), default="", blank=False
    )

    last_name = models.CharField(
        max_length=64, default="", verbose_name=_("Last name"), blank=False
    )

    # ----- Registration information -----

    educational_institution = models.CharField(
        max_length=20, verbose_name=_("Educational institution"), blank=True
    )

    study_programme = models.CharField(
        max_length=20, verbose_name=_("Study programme"), blank=True
    )

    student_number = models.CharField(
        verbose_name=_("Student number"),
        max_length=8,
        validators=[
            validators.RegexValidator(
                regex=r"(s\d{7}|[ezu]\d{6,7})",  # TODO: allow for HAN, maybe others
                message=_("Enter a valid student- or e/z/u-number."),  # or no check
            )
        ],
        blank=True,
        unique=True,
    )

    RSC_number = models.CharField(
        verbose_name=_("RSC card number"), max_length=9, blank=True, unique=True
    )

    payment_method = models.CharField(choices=PaymentMethods.choices, max_length=2)

    # ---- Personal information ------

    IBAN = IBANField()

    birthday = models.DateField(verbose_name=_("Birthday"), null=True)

    gender = models.CharField(choices=Genders.choices, max_length=1)

    show_birthday = models.BooleanField(
        verbose_name=_("Display birthday"),
        help_text=_(
            "Show your birthday to other members on your profile page and "
            "in the birthday calendar"
        ),
        default=True,
    )

    profile_description = models.TextField(
        verbose_name=_("Profile text"),
        help_text=_("Text to display on your profile"),
        blank=True,
        max_length=4096,
    )

    initials = models.CharField(max_length=20, verbose_name=_("Initials"), blank=True)

    nickname = models.CharField(max_length=30, verbose_name=_("Nickname"), blank=True)

    display_name_preference = models.CharField(
        max_length=10,
        verbose_name=_("How to display name"),
        choices=(
            ("full", _("Show full name")),
            ("nickname", _("Show only nickname")),
            ("firstname", _("Show only first name")),
            ("initials", _("Show initials and last name")),
            ("fullnick", _("Show name like \"John 'nickname' Doe\"")),
            ("nicklast", _("Show nickname and last name")),
        ),
        default="full",
    )


class Organisation(Contact):
    name = models.CharField(max_length=100, verbose_name=_("Organisation name"))

    website = models.URLField(verbose_name=_("Website"), blank=True)

    def __str__(self):
        return f"Organisation {self.name}"
