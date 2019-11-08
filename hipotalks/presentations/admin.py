from django.contrib import admin

from hipotalks.presentations.models import Presentation


class PresentationAdmin(admin.ModelAdmin):
    list_display = ('title', 'slide_link', 'video_link')
    readonly_fields = ('creation_datetime', 'update_datetime')


admin.site.register(Presentation, PresentationAdmin)
