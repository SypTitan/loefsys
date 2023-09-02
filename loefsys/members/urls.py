from django.urls import path, include

from members.views import ProfileDetailView, ProfileListView

app_name = "members"

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
