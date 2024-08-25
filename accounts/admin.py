from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.models import User, UserProfile

# Register your models here.


class CustomUserAdmin(UserAdmin):
    filter_horizontal = ()
    list_filter = ()
    ordering = ("-date_joined",)
    fieldsets = ()
    list_display = (
        "email",
        "first_name",
        "last_name",
        "username",
        "role",
        "is_active",
        "is_superadmin",
    )


admin.site.register(User, CustomUserAdmin)
admin.site.register(UserProfile)
