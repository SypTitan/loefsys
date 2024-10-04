"""Module containing the definition for a person."""

from typing import TYPE_CHECKING, Optional

from django.db import models
from django.db.models import F, Value, When
from django.db.models.functions import Concat
from django.utils.translation import gettext_lazy as _
from django_extensions.db.models import TimeStampedModel

from loefsys.contacts.models.choices import DisplayNamePreferences

from .contact import Contact

if TYPE_CHECKING:
    from loefsys.contacts.models.member import LoefbijterMember


class Person(TimeStampedModel):
    """A concrete version of a contact representing a person.

    This instance is used both for members of Loefbijter and guests. The distinction
    between the two cases can be found with the presence of the `member` attribute,
    which will only exist if the person is a member. A utility function is provided with
    `is_member`.

    TODO write tests for the GeneratedField logic.

    Attributes
    ----------
    created : ~datetime.datetime
        The timestamp of the creation of this model.
    modified : ~datetime.datetime
        The timestamp of last modification of this model.
    contact : ~loefsys.contacts.models.contact.Contact
        The contact details belonging to this person.
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
    """

    contact = models.OneToOneField(to=Contact, on_delete=models.CASCADE)

    first_name = models.CharField(max_length=64, verbose_name=_("First name"))
    last_name = models.CharField(max_length=64, verbose_name=_("Last name"))
    initials = models.CharField(max_length=20, verbose_name=_("Initials"), blank=True)
    nickname = models.CharField(max_length=30, verbose_name=_("Nickname"), blank=True)
    display_name_preference = models.PositiveSmallIntegerField(
        choices=DisplayNamePreferences, default=DisplayNamePreferences.FULL
    )
    display_name = models.GeneratedField(
        expression=models.Case(
            models.When(
                display_name_preference=DisplayNamePreferences.FULL_WITH_NICKNAME,
                then=Concat(
                    F("first_name"),
                    Value(" '"),
                    F("nickname"),
                    Value("' "),
                    F("last_name"),
                ),
            ),
            When(
                display_name_preference=DisplayNamePreferences.NICKNAME_LASTNAME,
                then=Concat(F("nickname"), Value(" "), F("last_name")),
            ),
            When(
                display_name_preference=DisplayNamePreferences.INITIALS_LASTNAME,
                then=Concat(F("initials"), Value(" "), F("last_name")),
            ),
            When(
                display_name_preference=DisplayNamePreferences.FIRSTNAME_ONLY,
                then=F("first_name"),
            ),
            When(
                display_name_preference=DisplayNamePreferences.NICKNAME_ONLY,
                then=F("nickname"),
            ),
            default=Concat(F("first_name"), Value(" "), F("last_name")),
        ),
        output_field=models.CharField(max_length=128),
        db_persist=True,
    )

    member: Optional["LoefbijterMember"]

    @property
    def is_member(self):
        """Determine whether the person is a member of Loefbijter."""
        return hasattr(self, "member")
