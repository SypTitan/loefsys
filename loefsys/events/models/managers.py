"""Module containing all model managers for the events app."""

from typing import TYPE_CHECKING

from django.db import models
from django.db.models import Q, QuerySet
from django.db.models.functions import Now

from .choices import RegistrationStatus

if TYPE_CHECKING:
    from .event import Event
    from .registration import EventRegistration


class EventManager[TEvent: "Event"](models.Manager[TEvent]):
    """Model manager for events."""

    def active(self) -> QuerySet[TEvent]:
        """Filter for events that are going to happen or are currently ongoing.

        Returns
        -------
        ~django.db.models.query.QuerySet of ~loefsys.events.models.event.Event
            A query of all active events.
        """
        return self.filter(event_end__lte=Now())


class EventRegistrationManager(models.Manager["EventRegistration"]):
    """Custom manager for :class:`~loefsys.events.models.EventRegistration` models."""

    def order_by_creation(self) -> QuerySet["EventRegistration"]:
        """Allows a query to be sorted by creation.

        Returns
        -------
        ~django.db.models.query.QuerySet of ~loefsys.events.models.EventRegistration
            A query sorted by creation timestamp.
        """
        return self.order_by("created")

    def active(self) -> QuerySet["EventRegistration"]:
        """Filters and only returns active registrations.

        Returns
        -------
        ~django.db.models.query.QuerySet of ~loefsys.events.models.EventRegistration
            A query containing active registrations only.
        """
        return self.filter(status=RegistrationStatus.ACTIVE)

    def queued(self) -> QuerySet["EventRegistration"]:
        """Filters and only returns queued registrations.

        Returns
        -------
        ~django.db.models.query.QuerySet of ~loefsys.events.models.EventRegistration
            A query containing queued registrations only.
        """
        return self.filter(status=RegistrationStatus.QUEUED)

    def cancelled(self) -> QuerySet["EventRegistration"]:
        """Filters and only returns cancelled registrations.

        Returns
        -------
        ~django.db.models.query.QuerySet of ~loefsys.events.models.EventRegistration
            A query containing cancelled registrations only.
        """
        return self.filter(
            Q(status=RegistrationStatus.CANCELLED_FINE)
            | Q(status=RegistrationStatus.CANCELLED_NOFINE)
        )
