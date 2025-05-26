"""Admin configuration for the Reservation and Log models."""

from django.contrib import admin

from loefsys.reservations.models.log import Log, Question
from loefsys.reservations.models.user_log import UserLog

from .models import Boat, Material, ReservableType, Reservation, Room


@admin.register(Boat, Material, Room, ReservableType, Reservation)
class ReservationAdmin(admin.ModelAdmin):
    """Admin interface for the boat, material, room, reservabletype and reservation."""


class QuestionInline(admin.TabularInline):
    """Inline for questions."""

    model = Question
    extra = 1


class LogAdmin(admin.ModelAdmin):
    """Admin interface for creating a log."""

    inlines = (QuestionInline,)


admin.site.register(Log, LogAdmin)
admin.site.register(UserLog)
