from django.contrib import admin

from hipotalks.events.models import Event


class EventAdmin(admin.ModelAdmin):
    list_display = ('date', 'event_type', 'get_users', 'is_completed', 'get_canceled_users')
    list_filter = ('event_type', 'is_completed', 'users__username')

    def get_users(self, obj):
        return ', '.join([user.full_name for user in obj.users.all()])
    get_users.short_description = 'Users'

    def get_canceled_users(self, obj):
        return ', '.join([user.full_name for user in obj.canceled_users.all()])
    get_canceled_users.short_description = 'Canceled Users'


admin.site.register(Event, EventAdmin)