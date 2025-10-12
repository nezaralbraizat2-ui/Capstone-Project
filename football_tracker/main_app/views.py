from ast import Match
from django.shortcuts import get_object_or_404, redirect, render

from django.views.generic import ListView, DetailView

from .forms import MatchForm
from .models import Team, Player, Match
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.



def add_player_to_match(request, player_id, match_id):
    player = Player.objects.get(id=player_id)
    match = Match.objects.get(id=match_id)
    match.players.add(player)
    return redirect('player-detail', pk=player.id)


def remove_player_from_match(request, player_id, match_id):
    player = Player.objects.get(id=player_id)
    match = Match.objects.get(id=match_id)
    match.players.remove(player) 
    return redirect('player-detail', pk=player.id)



def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')



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
        new_match = form.save(commit=False)  # لم يتم الحفظ بعد
        new_match.team_id = team_id           # ربط بالمباراة بالفريق
        new_match.created_by = request.user   # ربط بالمستخدم الحالي
        new_match.save()                      # الآن نحفظه في قاعدة البيانات
    return redirect('team-detail', team_id=team_id)

class PlayerCreate(CreateView):
    model = Player
    fields = ['name', 'position', 'jersey_number', 'team']
    success_url = reverse_lazy('player-index')

class PlayerDetail(DetailView):
    model = Player
    template_name = 'main_app/player_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        available_matches = Match.objects.exclude(players=self.object)
        context['matches'] = available_matches
        return context


class PlayerList(ListView):
    model = Player

class PlayerUpdate(UpdateView):
    model = Player
    fields = ['name', 'position', 'jersey_number']

class PlayerDelete(DeleteView):
    model = Player
    success_url = '/players/'

def cancel_match(request, match_id):
    match = Match.objects.get(id=match_id)
    team_id = match.home_team.id
    match.delete()  
    return redirect('team-detail', team_id=team_id)

