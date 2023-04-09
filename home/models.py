from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='category')

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,blank=True,null=True)
    name = models.CharField(max_length=200)
    amount = models.PositiveIntegerField()
    product_price = models.FloatField()
    discount = models.FloatField(blank=True,null=True)
    total_price = models.FloatField()
    description = models.TextField(blank=True,null=True)
    available = models.BooleanField(default= True)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='products')


    def __str__(self):
        return self.name

    def total_price(self):
        if not self.discount:
            return self.product_price
        elif self.discount:
            total = (self.product_price*self.discount)/100
            return float(self.product_price - total)
        return self.total_price