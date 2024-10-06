"""Module containing the model definition for the member model."""

from typing import TYPE_CHECKING, Optional

from django.db import models
from django.db.models import QuerySet
from django.utils.translation import gettext_lazy as _
from django_extensions.db.models import TimeStampedModel

from loefsys.contacts.models.choices import Genders
from loefsys.contacts.models.person import Person

if TYPE_CHECKING:
    from .membership import Membership
    from .study_registration import StudyRegistration


class LoefbijterMember(TimeStampedModel):
    """Model that defines the properties for a member of Loefbijter.

    This model contains the required details for a person to be a member of Loefbijter.
    Thus, it will only exist on a `Person` object when the person is a member.

    Attributes
    ----------
    person : ~loefsys.contacts.models.person.Person
        The person that the membership details are for.
    gender : ~loefsys.contacts.models.choices.Genders
        The gender of the person.
    birthday : ~datetime.date
        The birthday of the member.
    show_birthday : bool
        Flag to determine the person's preference to publicly show their birthday.

        If set to `True`, other people will be able to see this person's birthday in
        loefsys.
    study_registration: ~loefsys.contacts.models.study_registration.StudyRegistration \
        or None
        The study registration for this member.

        If this value is `None`, then this member does not study.
    """

    person = models.OneToOneField(
        to=Person, on_delete=models.CASCADE, related_name="member", primary_key=True
    )

    gender = models.PositiveSmallIntegerField(
        choices=Genders.choices, verbose_name=_("Gender")
    )
    birthday = models.DateField(verbose_name=_("Birthday"))
    show_birthday = models.BooleanField(verbose_name=_("Display birthday"))

    study_registration: Optional["StudyRegistration"]
    membership_set: QuerySet["Membership"]
