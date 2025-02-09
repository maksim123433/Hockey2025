from django.contrib import admin
from .models import Matches


class MatchesAdmin(admin.ModelAdmin):
    list_display = ("First_club", "Second_club", "Date", "Arbiter", "City")
    search_fields = ("First_club__Name", "Second_club__Name")


admin.site.register(Matches, MatchesAdmin)
