from ast import Match
from django.shortcuts import get_object_or_404, redirect, render

from django.views.generic import ListView, DetailView

from .forms import MatchForm
from .models import Team, Player, Match
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


@login_required
def add_player_to_match(request, player_id, match_id):
    player = Player.objects.get(id=player_id)
    match = Match.objects.get(id=match_id)
    match.players.add(player)
    return redirect('player-detail', pk=player.id)

@login_required
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

@login_required
def team_index(request):
    teams = Team.objects.filter(user=request.user)
    return render(request, 'teams/index.html', {'teams': teams})

@login_required
def team_detail(request, team_id):
    team = Team.objects.get(id=team_id)
    match_form = MatchForm()
    return render(request, 'teams/detail.html', { 'team': team, 'match_form': match_form })

class TeamCreate(CreateView):
    model = Team
    fields = ['name', 'country', 'coach_name', 'stadium', 'image']
    success_url = reverse_lazy('team-index')


    def form_valid(self, form):
        form.instance.user = self.request.user
        
        return super().form_valid(form)



class TeamUpdate(LoginRequiredMixin,UpdateView):
    model = Team
    fields = [ 'country', 'coach_name', 'stadium', 'image']
    success_url = reverse_lazy('team-index')

class TeamDelete(LoginRequiredMixin,DeleteView):
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

class PlayerCreate(LoginRequiredMixin,CreateView):
    model = Player
    fields = ['name', 'position', 'jersey_number', 'team']
    success_url = reverse_lazy('player-index')

class PlayerDetail(LoginRequiredMixin,DetailView):
    model = Player
    template_name = 'main_app/player_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        available_matches = Match.objects.exclude(players=self.object)
        context['matches'] = available_matches
        return context


class PlayerList(LoginRequiredMixin,ListView):
    model = Player

class PlayerUpdate(LoginRequiredMixin,UpdateView):
    model = Player
    fields = ['name', 'position', 'jersey_number']

class PlayerDelete(LoginRequiredMixin,DeleteView):
    model = Player
    success_url = '/players/'

def cancel_match(request, match_id):
    match = Match.objects.get(id=match_id)
    team_id = match.home_team.id
    match.delete()  
    return redirect('team-detail', team_id=team_id)

class Home(LoginView):
    template_name = 'home.html'




def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('team-index')
        else:
            error_message = 'Invalid sign up - try again'
    else:
        form = UserCreationForm()
    
    context = {
        'form': form,
        'error_message': error_message
    }
    return render(request, 'signup.html', context)


















# def signup(request):
#     error_message = ''
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('team-index')
#         else:
#             error_message = 'Invalid sign up - try again'
#     form = UserCreationForm()
#     context = {'form': form, 'error_message': error_message}
#     return render(request, 'signup.html', context)
   