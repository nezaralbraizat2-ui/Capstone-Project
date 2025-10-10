from django.db import models
from django.urls import reverse

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

    def __str__(self):
        return self.name
    


def get_absolute_url(self):

    return reverse('team-detail', kwargs={'team_id': self.id})


class Match(models.Model):
    date = models.DateField('match date')
    home_team = models.ForeignKey(Team, related_name='home_matches', on_delete=models.CASCADE)
    away_team = models.ForeignKey(Team, related_name='away_matches', on_delete=models.CASCADE)
    home_score = models.IntegerField(null=True, blank=True)
    away_score = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.home_team} vs {self.away_team} on {self.date}"
    
    class Meta:
        ordering = ['-date']