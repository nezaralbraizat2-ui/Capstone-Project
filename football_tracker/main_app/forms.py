from django import forms
from .models import Match
from django.contrib.auth.models import User

class MatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ['date', 'home_team', 'away_team', 'home_score', 'away_score']
        widgets = {
            'date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'placeholder': 'Select a date',
                    'type': 'date'
                }
            ),
        }

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
