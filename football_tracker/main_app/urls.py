from django.urls import path, include
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),

    path('teams/', views.team_index, name='team-index'),
    path('teams/<int:team_id>/', views.team_detail, name='team-detail'),
    path('teams/create/', views.TeamCreate.as_view(), name='team-create'),
    path('teams/<int:pk>/update/', views.TeamUpdate.as_view(), name='team-update'),
    path('teams/<int:pk>/delete/', views.TeamDelete.as_view(), name='team-delete'),
    path('teams/<int:team_id>/add-match/', views.add_match, name='add-match'),

    path('players/create/', views.PlayerCreate.as_view(), name='player-create'),
    path('players/<int:player_id>/add_match/<int:match_id>/', views.add_player_to_match, name='add_player_to_match'),  # ضعها هنا قبل player-detail
    path('players/<int:pk>/', views.PlayerDetail.as_view(), name='player-detail'),
    path('players/', views.PlayerList.as_view(), name='player-index'),
    path('players/<int:pk>/update/', views.PlayerUpdate.as_view(), name='player-update'),
    path('players/<int:pk>/delete/', views.PlayerDelete.as_view(), name='player-delete'),
    path('players/<int:player_id>/remove_from_match/<int:match_id>/', views.remove_player_from_match, name='remove_player_from_match'),
    path('matches/<int:match_id>/cancel/', views.cancel_match, name='cancel-match'),

    path('admin/', admin.site.urls),
    path('accounts/signup/', views.signup, name='signup'),
    path('profile/', views.profile_view, name='profile'),
     path('logout/', auth_views.LogoutView.as_view(), name='logout'),
      path('password_change/', auth_views.PasswordChangeView.as_view(template_name='users/password_change.html'), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'), name='password_change_done'),
]

