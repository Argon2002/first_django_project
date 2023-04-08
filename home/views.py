from django.shortcuts import render
from django.http import  HttpResponse
from .models import *


def home(requset):
    category = Category.objects.all()
    return render(requset,'home/Home.html',{'category':category})

def product(requset):
    return render(requset,"home/Product.html")

def argon(requset):
    return  HttpResponse("Welcome To Argon Page")

# Create your views here.
