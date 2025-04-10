from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from profil.models import CustomUser


# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'first_name', 'last_name', ]
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone_number', 'address', 'image')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('phone_number', 'address', 'image')}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
