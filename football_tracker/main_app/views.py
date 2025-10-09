from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return HttpResponse("Welcome to the Football Tracker!")

def about(request):
    return render(request, 'about.html')

class Team:
    def __init__(self, name, country, coach_name, stadium=None):
        self.name = name
        self.country = country
        self.coach_name = coach_name
        self.stadium = stadium


# Create the teams list after the Team class is defined so we can instantiate Team
Team.teams = [
    Team("barcelona", "Spain", "hansi Flick", "Camp Nou"),
    Team("man-united", "England", "ruben amorim", "Old Trafford"),
    Team("man-city", "England", "Pep Guardiola", "Etihad Stadium"),
    Team("real-madrid", "Spain", "xabi alonso", "Santiago Bernabéu"),
]


def team_index(request):
    return render(request, 'teams/index.html', { 'teams': Team.teams })