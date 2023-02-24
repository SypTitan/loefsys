from django.contrib import admin

from .models import Committee, CommitteeMembership


class CommitteeInline(admin.TabularInline):
    model = CommitteeMembership
    extra = 0
    # list_filter
    ordering = ("-is_head", "since")

    def get_queryset(self, request):
        return super(CommitteeInline, self).get_queryset(request).filter(until=None)

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser


class CommitteeAdmin(admin.ModelAdmin):
    inlines = [CommitteeInline]


admin.site.register(Committee, CommitteeAdmin)
