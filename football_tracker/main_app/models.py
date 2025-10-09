from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    coach_name = models.CharField(max_length=100)
    stadium = models.CharField(max_length=100, null=True, blank=True)
    image = models.CharField(max_length=255, null=True, blank=True)  # optional image path (relative to static/)

    def __str__(self):
        return self.name