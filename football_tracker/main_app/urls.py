from django.urls import path, include
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('teams/', views.team_index, name='team-index'),
    path('teams/<int:team_id>/', views.team_detail, name='team-detail'),
    path('admin/', admin.site.urls),
]
