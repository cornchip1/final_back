from django.db import models
from django.conf import settings
# Create your models here.

class Actor(models.Model):
    code = models.IntegerField(null=False)
    name = models.CharField(max_length=50)
    en_name = models.CharField(max_length=300)
    filmos = models.TextField()
    img = models.TextField(null=True, default="")