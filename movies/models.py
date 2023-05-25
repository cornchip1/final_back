from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Movie(models.Model):
    movie_id = models.IntegerField(blank=False)
    title = models.TextField(blank=False)
    genre_ids = models.TextField(null=True)
    overview = models.TextField(null=True)
    poster_path = models.TextField(null=True)
    release_date = models.DateField(null=True)
    vote_average = models.FloatField(null=True)
    directors = models.TextField(null=True)
    casts = models.TextField(null=True)
    video_key = models.TextField(null=True) 

class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rate = models.IntegerField(null=False, validators = [MaxValueValidator(5),MinValueValidator(0)])
    review = models.CharField(max_length=300, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Genre(models.Model):
    genre_id = models.IntegerField(null=False)
    name = models.TextField(null=False)
