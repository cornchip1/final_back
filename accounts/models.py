from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass

class Profile(models.Model):
    img = models.ImageField(upload_to='%Y/%m/%d',null=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)