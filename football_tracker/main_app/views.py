from django.shortcuts import redirect, render

from .forms import MatchForm
from .models import Team, Player
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.
def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


# class Team:
#     def __init__(self, name, country, coach_name, stadium=None, image=None):
#         self.name = name
#         self.country = country
#         self.coach_name = coach_name
#         self.stadium = stadium
#         # optional image path (relative to static/) to show on templates
#         self.image = image


# Create the teams list after the Team class is defined so we can instantiate Team
Team.teams = [
    Team("barcelona", "Spain", "hansi Flick", "Camp Nou", image='css/images/barcelona-logo.svg'),
    Team("man-united", "England", "ruben amorim", "Old Trafford", image='css/images/manchester-united.svg'),
    Team("man-city", "England", "Pep Guardiola", "Etihad Stadium", image='css/images/manchester-city-.svg'),
    Team("real-madrid", "Spain", "xabi alonso", "Santiago Bernabéu", image='css/images/real-madrid-.svg'),
]


def team_index(request):
    teams = Team.objects.all()
    return render(request, 'teams/index.html', {'teams': teams})

def team_detail(request, team_id):
    team = Team.objects.get(id=team_id)
    match_form = MatchForm()
    return render(request, 'teams/detail.html', { 'team': team, 'match_form': match_form })

class TeamCreate(CreateView):
    model = Team
    fields = '__all__'
    success_url = reverse_lazy('team-index')



class TeamUpdate(UpdateView):
    model = Team
    fields = [ 'country', 'coach_name', 'stadium', 'image']
    success_url = reverse_lazy('team-index')

class TeamDelete(DeleteView):
    model = Team
    success_url = '/teams/'


def add_match(request, team_id):
    form = MatchForm(request.POST)
    if form.is_valid():
        new_match = form.save(commit=False)
        new_match.team_id = team_id
        new_match.save()
    return redirect('team-detail', team_id=team_id)

class PlayerCreate(CreateView):
    model = Player
    fields = '__all__'