from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class UserAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    ordering = ('-date_joined',)
    readonly_fields = (
        'date_joined', 'last_login', 'created_date', 'modified_date'
    )
    fieldsets = (
        (('Personal Informations'), {
            'fields': ('email', 'username', 'first_name', 'last_name', 'phone_number', 'role',)
        }),
        (('Date Informations'), {
            'fields': ('date_joined', 'last_login', 'created_date', 'modified_date')
        }),
        (('Permissions Informations'), {
            'fields': ('is_admin', 'is_staff', 'is_active', 'is_superadmin')
        }),
    )
    list_filter = ['is_admin', 'is_staff', 'is_active', 'is_superadmin']
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
