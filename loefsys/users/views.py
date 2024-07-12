from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, ListView

from .models import User


class ProfileListView(ListView):
    template_name = "users/index.html"
    context_object_name = "users"

    # TODO broken function
    # def get_queryset(self):
    #    return User.objects.filter(member_until=None)


@method_decorator(login_required, "dispatch")  # TODO change to member_required
class ProfileDetailView(DetailView):
    """View that renders a member's profile."""

    model = User
    template_name = "users/profile.html"

    def setup(self, request, *args, **kwargs) -> None:
        if "pk" not in kwargs and request.user:
            kwargs["pk"] = request.user.pk
        super().setup(request, *args, **kwargs)
