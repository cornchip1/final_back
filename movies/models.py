from django.db import models
from django.conf import settings
# Create your models here.

class Movie(models.Model):
    title = models.TextField(blank=False)
    genre_ids = models.TextField(blank=True)
    overview = models.TextField(blank=True)
    poster_path = models.TextField(blank=True)
    release_date = models.DateField(blank=True)
    vote_average = models.FloatField(blank=True)

class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')
    rate = models.IntegerField(null=False)
    review = models.CharField(max_length=300, null=True)