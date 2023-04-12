from django.shortcuts import render,get_object_or_404
from django.http import  HttpResponse
from .models import *


def home(requset):
    category = Category.objects.all()
    return render(requset,'home/Home.html',{'category':category})

def all_products(requset,slug=None,id= None):

    products = Product.objects.all()
    category = Category.objects.all()
    if slug and id:
        data = get_object_or_404(Category,slug=slug,id= id)
        products = products.filter(category=data)
    return render(requset,"home/Product.html", {'products': products,'category':category})

def product_detail(request,id):
    product = get_object_or_404(Product,id=id)
    return render(request,"home/ProductDetail.html",{'product':product})

def argon(requset):
    return  HttpResponse("Welcome To Argon Page")

# Create your views here.
