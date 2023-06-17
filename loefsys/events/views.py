from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.db.models import F
from django.shortcuts import redirect, get_object_or_404

from django.utils import timezone
from django.utils.decorators import method_decorator
from django.utils.translation import gettext_lazy as _

from django.views import View
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView

from . import services
from .models import Event, EventRegistration, GuestContactDetails


class EventListView(ListView):
    template_name = "events/index.html"
    context_object_name = "events"

    def get_queryset(self):
        return Event.objects.annotate(future=F("start")).filter(
            future__gt=timezone.now()
        )


@method_decorator(login_required, "dispatch")
class EventDetailView(DetailView):
    """View that renders a member's profile."""

    model = Event
    queryset = Event.objects.filter(published=True)
    template_name = "events/event.html"
    context_object_name = "event"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = self.request.user
        # context["payment_method_tpay"] = Payment.TPAY

        event = context["event"]
        if event.max_participants:
            perc = 100.0 * len(event.participants) / event.max_participants
            context["registration_percentage"] = perc

        try:
            context["registration"] = EventRegistration.objects.get(
                event=event, user=self.request.user
            )
        except (EventRegistration.DoesNotExist, TypeError):
            pass

        # context["permissions"] = services.event_permissions(self.request.member, event)

        context["date_now"] = timezone.now()

        # context["slide_size"] = settings.THUMBNAIL_SIZES["slide"]

        context["participants"] = event.participants.select_related(
            "member", "member__profile"
        )

        return context


@method_decorator(login_required, name="dispatch")
class EventRegisterView(View):
    """Define a view that allows the user to register for an event using a POST request.

    The user should be authenticated.
    """

    def get(self, request, *args, **kwargs):
        return redirect("events:event", pk=kwargs["pk"])

    def post(self, request, *args, **kwargs):
        event = get_object_or_404(Event, pk=kwargs["pk"])
        print("POST")
        try:
            services.create_registration(request.user, event)

            if not (request.user.member or request.user.guest_form):
                return redirect("events:registration", event.pk)

            if (not request.user.member) and request.user.guest_form:
                if (
                    event.price > 0
                    or event.fine > 0
                    and not request.user.guest_form.IBAN
                ):
                    # TODO add message for IBAN required.
                    return redirect("events:registration", event.pk)
                # if address_required becomes a thing, add a check here.

            messages.success(request, _("Registration successful."))
            print("succes")
        except Exception as e:
            messages.error(request, e)
            print("failure")

        return redirect(event)


# TODO fix this somehow, this is should redirect back to the event.
class EventGuestContactCreateView(LoginRequiredMixin, CreateView):
    form_class = GuestContactDetails
    exclude = ["user"]

    def form_valid(self, form):
        form.user = self.request.user
        return super().form_valid(form)
