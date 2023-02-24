from django.urls import path, include

from events.views import (
    EventListView,
    EventDetailView,
    EventRegisterView,
    EventGuestContactCreateView,
)

app_name = "events"

urlpatterns = [
    path(
        "",
        include(
            [
                path("", EventListView.as_view(), name="events"),
                path("<int:pk>/", EventDetailView.as_view(), name="event"),
                path(
                    "<int:pk>/registration/register/",
                    EventRegisterView.as_view(),
                    name="register",
                ),
                # path(
                #     "<int:pk>/registration/cancel/",
                #     EventCancelView.as_view(),
                #     name="cancel",
                # ),
                path(
                    "<int:pk>/registration/",
                    EventGuestContactCreateView.as_view(),
                    name="registration",
                ),
            ]
        ),
    ),
]
