from django.contrib import admin
from .models import Clubs


class ClubsAdmin(admin.ModelAdmin):
    list_display = ("Name", "Foundation_date", "Head_coach", "Conference")
    search_fields = ("Name", "Head_coach")


admin.site.register(Clubs, ClubsAdmin)
