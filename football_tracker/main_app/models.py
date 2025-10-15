from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save

from django.dispatch import receiver

# Create your models here.




ATCH_TYPES = (
    ('L', 'League'),
    ('F', 'Friendly'),
    ('C', 'Cup')
)


class Team(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    coach_name = models.CharField(max_length=100)
    stadium = models.CharField(max_length=100, null=True, blank=True)
    image = models.CharField(max_length=255, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    


def get_absolute_url(self):

    return reverse('team-detail', kwargs={'team_id': self.id})



class Player(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    jersey_number = models.IntegerField(null=True, blank=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='players')

    def __str__(self):
        return reverse('player-detail', kwargs={'pk': self.id})





class Match(models.Model):
    date = models.DateField('match date')
    home_team = models.ForeignKey(Team, related_name='home_matches', on_delete=models.CASCADE)
    away_team = models.ForeignKey(Team, related_name='away_matches', on_delete=models.CASCADE)
    home_score = models.IntegerField(null=True, blank=True)
    away_score = models.IntegerField(null=True, blank=True)
    created_by = models.ForeignKey(User, related_name='matches_created', on_delete=models.CASCADE)
    players = models.ManyToManyField(Player, related_name='matches', blank=True) 

    def __str__(self):
        return f"{self.home_team} vs {self.away_team} on {self.date}"
    
    class Meta:
        ordering = ['-date']


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_pics/', default='profile_pics/default.png')

    def __str__(self):
        return f"{self.user.username} Profile"


# ✅ Signal: Create profile automatically when user is created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# ✅ Signal: Save profile when user is saved
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()