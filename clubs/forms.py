from django import forms
from django.forms import ModelForm
from .models import Clubs

class ClubsForm(ModelForm):
    class Meta:
        model = Clubs
        fields = (
            "Name",
            "Foundation_date",
            "Head_coach",
            "Number_of_players",
            "Owner",
            "Conference",
            "Total_cost_of_club",
        )

