from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='category')

    def __str__(self):
        return self.name

