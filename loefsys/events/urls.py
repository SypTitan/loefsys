"""Module containing the url definition of the events app."""

from django.urls import path

from .views import CalendarView, EventFillerView, EventView, RegistrationFormView

app_name = "events"

urlpatterns = [
    path("<int:pk>/", EventView.as_view(), name="event"),
    path("<slug:slug>/", EventView.as_view(), name="event"),
    # path("<int:pk>/register/", None, name="register"),
    # path("<slug:slug>/registration/cancel", None, name="cancel"),
    path(
        "<slug:slug>/registration/", RegistrationFormView.as_view(), name="registration"
    ),
    path("", CalendarView.as_view(), name="events"),
    path("event_filler", EventFillerView.as_view(), name="event_filler"),
]
