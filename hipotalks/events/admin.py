from django.contrib import admin

from hipotalks.events.models import Event


class EventAdmin(admin.ModelAdmin):
    list_display = ('date', 'event_type',)
    list_filter = ('event_type', )
    readonly_fields = ('creation_datetime', 'update_datetime')


admin.site.register(Event, EventAdmin)