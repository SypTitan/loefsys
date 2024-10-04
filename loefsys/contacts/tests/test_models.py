from cfgv import ValidationError
from django.test import TestCase
from django_dynamic_fixture import G, N

from loefsys.contacts.models import Address, LoefbijterMember, Membership, Person
from loefsys.contacts.models.contact import Contact
from loefsys.contacts.models.organization import Organization
from loefsys.contacts.models.study_registration import StudyRegistration


class AddressTestCase(TestCase):
    def test_create(self):
        address = G(Address)
        self.assertIsNotNone(address)
        self.assertIsNotNone(address.pk)


class ContactTestCase(TestCase):
    def test_create(self):
        contact = G(Contact)
        self.assertIsNotNone(contact)
        self.assertIsNotNone(contact.pk)

    def test_validation_no_relation(self):
        contact = N(Contact)
        self.assertRaises(ValidationError, contact.full_clean)

    def test_validation_organization(self):
        contact = N(Contact)
        _ = N(Organization, contact=contact)
        try:
            contact.full_clean()
        except ValidationError:
            self.fail("Exception was thrown")

    def test_validation_person(self):
        contact = N(Contact)
        _ = N(Person, contact=contact)
        try:
            contact.full_clean()
        except ValidationError:
            self.fail("Exception was thrown")

    def test_validation_organization_person(self):
        contact = N(Contact)
        _ = N(Organization, contact=contact)
        _ = N(Person, contact=contact)
        self.assertRaises(ValidationError, contact.full_clean)


class LoefbijterMemberTestCase(TestCase):
    def test_create(self):
        member = G(LoefbijterMember)
        self.assertIsNotNone(member)
        self.assertIsNotNone(member.pk)


class MembershipTestCase(TestCase):
    def test_create(self):
        membership = G(Membership)
        self.assertIsNotNone(membership)
        self.assertIsNotNone(membership.pk)


class OrganizationTestCase(TestCase):
    def test_create(self):
        organization = G(Organization)
        self.assertIsNotNone(organization)
        self.assertIsNotNone(organization.pk)


class PersonTestCase(TestCase):
    def test_create(self):
        person = G(Person)
        self.assertIsNotNone(person)
        self.assertIsNotNone(person.pk)


class StudyRegistrationTestCase(TestCase):
    def test_create(self):
        registration = G(StudyRegistration)
        self.assertIsNotNone(registration)
        self.assertIsNotNone(registration.pk)
