from django.db import models
from django.urls import reverse
# Create your models here.
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