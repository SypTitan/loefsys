from django.urls import include, path
from rest_framework import routers
from .views import UserViewSet

from loefsys.users.views import (
    user_detail_view,
    user_redirect_view,
    user_update_view,
)

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

app_name = "users"
# urlpatterns = [
#     path("~redirect/", view=user_redirect_view, name="redirect"),
#     path("~update/", view=user_update_view, name="update"),
#     path("<str:username>/", view=user_detail_view, name="detail"),
# ]

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
