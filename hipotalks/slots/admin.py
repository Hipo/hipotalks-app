from django.contrib import admin

from hipotalks.slots.models import Slot


class SlotAdmin(admin.ModelAdmin):
    list_display = ('user', 'event', 'status', 'presentation', 'creation_datetime')
    list_filter = ('user', 'status')
    readonly_fields = ('creation_datetime', 'update_datetime')


admin.site.register(Slot, SlotAdmin)