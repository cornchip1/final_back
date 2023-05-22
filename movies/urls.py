# from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.urls import path
from . import views

urlpatterns = [
    path('<int:movie_id>/', views.movie_detail),
    path('<int:movie_id>/review/', views.review_create),
    path('reviews/<int:review_id>/', views.review_detail),

]
