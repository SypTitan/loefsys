from django.contrib import admin

from .models import Event, EventRegistration


class RegistrationInline(admin.TabularInline):
    model = EventRegistration
    extra = 0
    # list_filter
    # ordering = ('-is_head', 'since')

    # def get_queryset(self, request):
    #     return super(RegistrationInline, self)\
    #         .get_queryset(request).filter(until=None)

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser


class EventAdmin(admin.ModelAdmin):
    list_display = ["title", "start"]
    inlines = [RegistrationInline]


admin.site.register(Event, EventAdmin)
