from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User,models.CASCADE)
    phone = models.IntegerField(null=True,blank=True)
    address = models.TextField(max_length=300,null=True,blank=True)
