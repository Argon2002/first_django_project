from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Profile(models.Model):
    user = models.OneToOneField(User,models.CASCADE)
    phone = models.IntegerField(null=True,blank=True)
    address = models.TextField(max_length=300,null=True,blank=True)

    def __str__(self):
        return self.user.username

def save_profile_user(sender,**kwargs):
    if kwargs['created']:
        profile_user= Profile(user=kwargs['instance'])
        profile_user.save()


post_save.connect(save_profile_user,sender=User)


