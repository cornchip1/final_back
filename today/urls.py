# from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.urls import path
from . import views

urlpatterns = [
    path('random/', views.random_movie),
    path('movies/', views.random_movies),
    path('movies/results/<int:movie_id>/', views.movies_result),
    path('actors/', views.random_actors),
    path('actors/results/<int:actor_id>/', views.actors_result),
]
