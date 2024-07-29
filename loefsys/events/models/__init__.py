"""Module containing the models related to events."""

from .event import OptionalRegistrationEvent, RequiredRegistrationEvent
from .registration import EventRegistration

__all__ = [
    "RequiredRegistrationEvent",
    "OptionalRegistrationEvent",
    "EventRegistration",
]
