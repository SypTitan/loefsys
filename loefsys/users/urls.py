from django.urls import include, path

from .views import ProfileDetailView, ProfileListView

app_name = "users"

urlpatterns = [
    path("", ProfileListView.as_view(), name="members"),
    path(
        "",
        include(
            [
                path("profile/", ProfileDetailView.as_view(), name="profile"),
                path("profile/<int:pk>", ProfileDetailView.as_view(), name="profile"),
            ]
        ),
    ),
]
