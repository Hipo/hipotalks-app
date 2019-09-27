from django.contrib import admin

from hipotalks.blacklist.models import Blacklist


class BlacklistAdmin(admin.ModelAdmin):
    list_display = ('user', 'event')
    list_filter = ('user',)


admin.site.register(Blacklist, BlacklistAdmin)