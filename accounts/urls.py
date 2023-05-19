from django.urls import path
from . import views

urlpatterns = [
    path('user/<int:user_pk>/',views.profile_detail),
] 
