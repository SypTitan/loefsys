from collections import OrderedDict

from django.db.models import Q
from django.utils import timezone
from django.utils.datetime_safe import date
from django.utils.translation import gettext_lazy as _

from events.models import (
    EventRegistration,
    Event,
)


def is_user_registered(user, event):
    """Return if the user is registered for the specified event.

    :param user: the user
    :param event: the event
    :return: None if registration is not required or no member else True/False
    """
    if not user.is_authenticated:
        return None

    return event.registrations.filter(user=user, date_cancelled=None).count() > 0


def user_registration_pending(user, event):
    """Return if the user is in the queue, but not yet registered for, the specific event.

    :param user: the user
    :param event: the event
    :return: None if registration is not required or no member else True/False
    """
    if not event.registration_required:
        return False
    if not user.is_authenticated:
        return None
    if event.max_participants is None:
        return False
    try:
        registration = event.active_registrations.get(user=user)
        return event.queue.index(registration)
    except EventRegistration.DoesNotExist:
        return False
    except ValueError:
        return False


def is_user_present(user, event):
    if not event.registration_required or not user.is_authenticated:
        return None

    return (
        event.registrations.filter(user=user, date_cancelled=None, present=True).count()
        > 0
    )


def is_organiser(member, event):
    if member and member.is_authenticated:
        if member.is_superuser or member.has_perm("events.override_organiser"):
            return True

        if event:
            return member.get_member_groups().filter(pk=event.organiser.pk).count() != 0

    return False


def create_registration(user, event):
    """Create a new user registration for an event.

    :param user: the user
    :param event: the event
    :return: Return the registration if successful
    """

    # TODO optimize this mess
    registration = None
    try:
        registration = EventRegistration.objects.get(event=event, user=user)
    except EventRegistration.DoesNotExist:
        pass

    if not event.optional_registrations:
        if event.registration_start < timezone.now() < event.registration_end:
            if registration is None:
                return EventRegistration.objects.create(event=event, user=user)
            if registration.date_cancelled is not None:
                registration.date = timezone.now()
                registration.date_cancelled = None
                registration.save()
        return registration

    elif timezone.now() < event.start:  # optional_registrations is True
        if registration is None:
            return EventRegistration.objects.create(event=event, user=user)

    return registration


# def cancel_registration(member, event):
#     """Cancel a user registration for an event.
#
#     :param member: the user
#     :param event: the event
#     """
#     registration = None
#     try:
#         registration = EventRegistration.objects.get(event=event, member=member)
#     except EventRegistration.DoesNotExist:
#         pass
#
#     if registration:
#         if not registration.queue_position:
#             emails.notify_first_waiting(event)
#
#             if event.send_cancel_email and event.after_cancel_deadline:
#                 emails.notify_organiser(event, registration)
#
#         # Note that this doesn"t remove the values for the
#         # information fields that the user entered upon registering.
#         # But this is regarded as a feature, not a bug. Especially
#         # since the values will still appear in the backend.
#         registration.date_cancelled = timezone.now()
#         registration.save()
#     else:
#         raise RegistrationError(_("You are not allowed to deregister for this event."))


# def update_registration(
#     member=None, event=None, name=None, registration=None, field_values=None, actor=None
# ):
#     """Update a user registration of an event.
#
#     :param member: the user
#     :param event: the event
#     :param name: the name of a registration not associated with a user
#     :param registration: the registration
#     :param field_values: values for the information fields
#     :param actor: Member executing this action
#     """
#     if not registration:
#         try:
#             registration = EventRegistration.objects.get(
#                 event=event, member=member, name=name
#             )
#         except EventRegistration.DoesNotExist as error:
#             raise RegistrationError(
#                 _("You are not registered for this event.")
#             ) from error
#     else:
#         member = registration.member
#         event = registration.event
#         name = registration.name
#
#     if not actor:
#         actor = member
#
#     permissions = event_permissions(actor, event, name)
#
#     if not field_values:
#         return
#     if not (permissions["update_registration"] or permissions["manage_event"]):
#         raise RegistrationError(_("You are not allowed to update this registration."))
#
#     for field_id, field_value in field_values:
#         field = RegistrationInformationField.objects.get(
#             id=field_id.replace("info_field_", "")
#         )
#
#         if (
#             field.type == RegistrationInformationField.INTEGER_FIELD
#             and field_value is None
#         ):
#             field_value = 0
#         elif (
#             field.type == RegistrationInformationField.BOOLEAN_FIELD
#             and field_value is None
#         ):
#             field_value = False
#         elif (
#             field.type == RegistrationInformationField.TEXT_FIELD
#             and field_value is None
#         ):
#             field_value = ""
#
#         field.set_value_for(registration, field_value)


# def registration_fields(request, member=None, event=None, registration=None, name=None):
#     """Return information about the registration fields of a registration.
#
#     :param member: the user (optional if registration provided)
#     :param name: the name of a non member registration
#                  (optional if registration provided)
#     :param event: the event (optional if registration provided)
#     :param registration: the registration (optional if member & event provided)
#     :return: the fields
#     """
#     if registration is None:
#         try:
#             registration = EventRegistration.objects.get(
#                 event=event, member=member, name=name
#             )
#         except EventRegistration.DoesNotExist as error:
#             raise RegistrationError(
#                 _("You are not registered for this event.")
#             ) from error
#         except EventRegistration.MultipleObjectsReturned as error:
#             raise RegistrationError(
#                 _("Unable to find the right registration.")
#             ) from error
#
#     member = registration.member
#     event = registration.event
#     name = registration.name
#
#     perms = event_permissions(member, event, name)[
#         "update_registration"
#     ] or is_organiser(request.member, event)
#     if perms and registration:
#         information_fields = registration.information_fields
#         fields = OrderedDict()
#
#         for information_field in information_fields:
#             field = information_field["field"]
#
#             fields[f"info_field_{field.id}"] = {
#                 "type": field.type,
#                 "label": field.name,
#                 "description": field.description,
#                 "value": information_field["value"],
#                 "required": field.required,
#             }
#
#         return fields
#     raise RegistrationError(_("You are not allowed to update this registration."))


# def update_registration_by_organiser(registration, member, data):
#     if not is_organiser(member, registration.event):
#         raise RegistrationError(_("You are not allowed to update this registration."))
#
#     if "payment" in data:
#         if data["payment"]["type"] == PaymentTypeField.NO_PAYMENT:
#             if registration.payment is not None:
#                 delete_payment(registration, member)
#         else:
#             registration.payment = create_payment(
#                 model_payable=registration,
#                 processed_by=member,
#                 pay_type=data["payment"]["type"],
#             )
#
#     if "present" in data:
#         registration.present = data["present"]
#
#     registration.save()


# def generate_category_statistics() -> dict:
#     """Generate statistics about events per category."""
#     current_year = datetime_to_lectureyear(timezone.now())
#
#     data = {
#         "labels": [str(current_year - 4 + i) for i in range(5)],
#         "datasets": [
#             {"label": str(display), "data": []}
#             for _, display in categories.EVENT_CATEGORIES
#         ],
#     }
#
#     for index, (key, _) in enumerate(categories.EVENT_CATEGORIES):
#         for i in range(5):
#             year_start = date(year=current_year - 4 + i, month=9, day=1)
#             year_end = date(year=current_year - 3 + i, month=9, day=1)
#
#             data["datasets"][index]["data"].append(
#                 Event.objects.filter(
#                     category=key, start__gte=year_start, end__lte=year_end
#                 ).count()
#             )
#
#     return data


# def execute_data_minimisation(dry_run=False):
#     """Delete information about very old events."""
#     # Sometimes years are 366 days of course, but better delete 1 or 2 days early than late
#     deletion_period = timezone.now().date() - timezone.timedelta(days=(365 * 5))
#
#     queryset = EventRegistration.objects.filter(event__end__lte=deletion_period).filter(
#         Q(payment__isnull=False) | Q(member__isnull=False) | ~Q(name__exact="<removed>")
#     )
#     if not dry_run:
#         queryset.update(payment=None, member=None, name="<removed>")
#     return queryset.all()
