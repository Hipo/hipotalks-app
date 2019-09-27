from django.contrib import admin

from hipotalks.presentations.models import Presentation


class PresentationAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'event', 'creation_datetime')
    list_filter = ('user',)


admin.site.register(Presentation, PresentationAdmin)