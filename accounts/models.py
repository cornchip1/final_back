from django.db import models
from django.contrib.auth.models import AbstractUser
from community.models import Article,Comment
from datetime import datetime

# Create your models here.
class User(AbstractUser):
    img = models.ImageField(upload_to='profile_img/%Y/%m/%d',null=True, default = 'default_profile.png')
    background_img = models.ImageField(upload_to='background_img/%Y/%m/%d',null=True, default = 'default_background.jpg')
    
# class Profile(models.Model):
#     user = models.OneToOneField(User,on_delete=models.CASCADE)
#     img = models.ImageField(upload_to='%Y/%m/%d')
#     # article = models.ManyToManyField(Article)
#     # comment = models.ManyToManyField(Comment)
 