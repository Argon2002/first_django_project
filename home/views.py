from django.shortcuts import render
from django.http import  HttpResponse


def home(requset):
    return render(requset,'home/Home.html')

def product(requset):
    return render(requset,"home/Product.html")

def argon(requset):
    return  HttpResponse("Welcome To Argon Page")

# Create your views here.
