from django.shortcuts import render
from django.http import  HttpResponse
from .models import *


def home(requset):
    category = Category.objects.all()
    return render(requset,'home/Home.html',{'category':category})

def all_products(requset,id=None):

    products = Product.objects.all()
    category = Category.objects.all()
    if id:
        data = Category.objects.get(id=id)
        products = products.filter(category=data)
    return render(requset,"home/Product.html", {'products': products,'category':category})

def product_detail(request,id):
    product = Product.objects.get(id=id)
    return render(request,"home/ProductDetail.html",{'product':product})

def argon(requset):
    return  HttpResponse("Welcome To Argon Page")

# Create your views here.
