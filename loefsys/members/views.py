from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, ListView

from .models import Member


class ProfileListView(ListView):
    template_name = "members/index.html"
    context_object_name = "members"

    def get_queryset(self):
        return Member.objects.filter(member_until=None)


@method_decorator(login_required, "dispatch")  # TODO change to member_required
class ProfileDetailView(DetailView):
    """View that renders a member's profile."""

    model = Member
    template_name = "members/profile.html"

    def setup(self, request, *args, **kwargs) -> None:
        if "pk" not in kwargs and request.user.member:
            kwargs["pk"] = request.user.member.pk
        super().setup(request, *args, **kwargs)
