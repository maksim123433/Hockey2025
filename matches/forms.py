from django import forms
from .models import Matches, Clubs


class CreateMatch(forms.ModelForm):
    class Meta:
        model = Matches
        fields = ['First_club', 'Second_club', 'Date', 'Arbiter', 'City']

