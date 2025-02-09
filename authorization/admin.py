from django.contrib import admin
from .models import ProUser


class AuthorizationAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "date_of_birth", "role")
    search_fields = ("first_name", "last_name")


admin.site.register(ProUser, AuthorizationAdmin)
