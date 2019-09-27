from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import ugettext_lazy as _

from .models import User


class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'full_name', 'is_active', 'is_staff', 'is_superuser')
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    search_fields = ('username', 'first_name', 'last_name')
    fieldsets = (
        (_(u'Base Informations'), {
            'fields': ('email', 'password'),
        }),
        (_(u'Personal Informations'), {
            'fields': (
                'username', 'first_name', 'last_name',
            )
        }),
        (_(u'General Informations'), {
            'fields': ('last_login', 'date_joined')
        }),
        (_(u'Permissions'), {
            'fields': (
                'is_active', 'is_staff',
                'is_superuser', 'groups', 'user_permissions'
            )
        }),
    )
    readonly_fields = ('last_login', 'date_joined')

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 'username', 'first_name', 'last_name',
                'password1', 'password2'
            )}
        ),
    )


admin.site.register(User, UserAdmin)