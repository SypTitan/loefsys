"""Module defining the models for contacts, both persons and organizations."""

from django.core import validators
from django.db import models
from django.db.models import Case, F, OneToOneField, When
from django.utils.translation import gettext_lazy as _
from django_extensions.db.models import TimeStampedModel
from phonenumber_field.modelfields import PhoneNumberField

from loefsys.users.models import User
from loefsys.users.models.choices import DisplayNamePreferences, Genders


class Address(TimeStampedModel):
    """Model that defines an address.

    Attributes
    ----------
    street : str
        The street and house number.
    street2 : str
        Additional information of the street if necessary.
    postal_code : str
        The postal code of the address.
    city : str
        The city that the address is located in.
    country : str
        The country that the city and address are located in.
    """

    street = models.CharField(
        max_length=100,
        validators=[
            validators.RegexValidator(
                regex=r"^.+ \d+.*", message=_("please use the format <street> <number>")
            )
        ],
        verbose_name=_("Street and house number"),
    )
    street2 = models.CharField(max_length=100, verbose_name=_("Second address line"))
    postal_code = models.CharField(max_length=10, verbose_name=_("Postal code"))
    city = models.CharField(max_length=50, verbose_name=_("City"))
    country = models.CharField(max_length=50)  # TODO maybe change to django-countries


class StudyRegistration(TimeStampedModel):
    """Model for persons who are registered for a study.

    Attributes
    ----------
    created : ~datetime.datetime
        The timestamp of creation of this model.
    modified : ~datetime.datetime
        The timestamp of last modification of this model.
    institution : str
        The name of the institution where the person is registered.
    programme : str
        The programme that the person follows at the institution.
    student_number : str
        The student number of the person.
    rsc_number : str
        The RSC number of the person or empty if they don't have one.
    """

    institution = models.CharField(
        max_length=32, verbose_name=_("Educational institution")
    )
    programme = models.CharField(max_length=32, verbose_name=_("Study programme"))
    student_number = models.CharField(
        max_length=10,
        verbose_name=_("Student number"),
        validators=[
            validators.RegexValidator(
                regex=r"(s\d{7}|[ezu]\d{6,7})",  # TODO: allow for HAN, maybe others
                message=_("Enter a valid student- or e/z/u-number."),  # or no check
            )
        ],
    )
    rsc_number = models.CharField(
        max_length=10, verbose_name=_("RSC card number"), blank=True
    )


class Contact(TimeStampedModel):
    """The base model defining a person or organization in the system.

    TODO @Mark expand on this.

    Attributes
    ----------
    created : ~datetime.datetime
        The timestamp of the creation of this model.
    modified : ~datetime.datetime
        The timestamp of last modification of this model.
    email : str
        The email for this contact.
    phone_number : str or None
        The phone number of this contact.
    address : ~loefsys.users.models.contact.Address or None
        The address of this contact.
    receive_newsletter : bool
        A flag that determines whether this contact wants to receive the newsletter.
    note : str
        An optional note about this user.
    user : ~loefsys.users.models.user.User or None
        The user account associated with this contact.
    """

    email = models.EmailField(_("email address"), unique=True)
    phone_number = PhoneNumberField(null=True)
    address = OneToOneField(to=Address, on_delete=models.SET_NULL, null=True)
    receive_newsletter = models.BooleanField(
        verbose_name=_("Receive newsletter"),
        help_text=_("Receive the Newsletter"),
        default=True,
    )
    note = models.TextField(max_length=500, blank=True)

    user = OneToOneField(to=User, on_delete=models.SET_NULL, null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return f"Contact information for {self.email}"

    def save(self, **kwargs):
        """Override of the save method.

        When a user is defined for this contact, then it automatically updates the email
        of the user account if it does not match the email of the contact.
        """
        if self.user and self.user.email != self.email:
            self.user.email = self.email
            self.user.save()
        super().save(**kwargs)


class Person(Contact):
    """A concrete version of a contact representing a person.

    Attributes
    ----------
    first_name : str
        The first name of the person.
    last_name : str
        The last name of the person.
    initials : str
        The initials of the first name (in Dutch 'voorletters').
    nickname : str
        The nickname of the person (in Dutch 'roepnaam').
    display_name_preference : ~loefsys.users.models.choices.DisplayNamePreferences
        The person's preference for having their name displayed.
    display_name : str
        A generated field that display's the person's name according to the preference.
    gender : ~loefsys.users.models.choices.Genders
        The gender of the person.
    birthday : ~datetime.date
        The person's birthday.
    show_birthday : bool
        Flag that show's whether the person wants their birthday publicly visible.
    study_registration : ~loefsys.users.models.contact.StudyRegistration or None
        The study registration for this person.
    """

    first_name = models.CharField(max_length=64, verbose_name=_("First name"))
    last_name = models.CharField(max_length=64, verbose_name=_("Last name"))
    initials = models.CharField(max_length=20, verbose_name=_("Initials"), blank=True)
    nickname = models.CharField(max_length=30, verbose_name=_("Nickname"), blank=True)
    display_name_preference = models.PositiveSmallIntegerField(
        choices=DisplayNamePreferences, default=DisplayNamePreferences.FULL
    )
    display_name = models.GeneratedField(
        expression=Case(
            When(
                display_name_preference=DisplayNamePreferences.FULL_WITH_NICKNAME,
                then=F("first_name") + " '" + F("nickname") + "' " + F("last_name"),
            ),
            When(
                display_name_preference=DisplayNamePreferences.NICKNAME_LASTNAME,
                then=F("nickname") + " " + F("last_name"),
            ),
            When(
                display_name_preference=DisplayNamePreferences.INITIALS_LASTNAME,
                then=F("initials") + " " + F("last_name"),
            ),
            When(
                display_name_preference=DisplayNamePreferences.FIRSTNAME_ONLY,
                then=F("first_name"),
            ),
            When(
                display_name_preference=DisplayNamePreferences.NICKNAME_ONLY,
                then=F("nickname"),
            ),
            default=F("first_name") + " " + F("last_name"),
        ),
        output_field=models.CharField(max_length=128),
        db_persist=True,
    )

    gender = models.CharField(choices=Genders.choices, verbose_name=_("Gender"))
    birthday = models.DateField(verbose_name=_("Birthday"), null=True, blank=True)
    show_birthday = models.BooleanField(verbose_name=_("Display birthday"))
    study_registration = models.OneToOneField(
        to=StudyRegistration, on_delete=models.SET_NULL, null=True, blank=True
    )


class Organization(Contact):
    """Model of a contact representing an organization.

    Attributes
    ----------
    name : str
        The organization's name.
    website : str
        The organization's website.
    """

    name = models.CharField(max_length=100, verbose_name=_("Organisation name"))
    website = models.URLField(verbose_name=_("Website"), blank=True)

    def __str__(self):
        return f"Organisation {self.name}"
