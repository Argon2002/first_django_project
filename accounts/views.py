from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def user_register(requset):
    if requset.method == 'POST':
        form = UserRegisterForm(requset.POST)
        if (form.is_valid()):
            data = form.cleaned_data
            User.objects.create_user(username=data["user_name"], email=data["email"], first_name=data["first_name"],
                                     last_name=data["last_name"], password=data["password_2"])
            return redirect('home:home')
    else:
        form = UserRegisterForm()

    context = {'form': form}
    return render(requset, 'accounts/Register.html', context)


def user_login(requset):
    if requset.method == 'POST':
        form = UserLoginForm(requset.POST)
        if form.is_valid():
            data = form.cleaned_data
            try:
                user = authenticate(requset, username=User.objects.get(email=data['user_name']),
                                    password=data['password'])
            except:

                user = authenticate(requset, username=data['user_name'], password=data['password'])
            if user is not None:
                login(requset, user)
                return redirect('home:home')

    else:
        form = UserLoginForm()

    return render(requset, 'accounts/Login.html', context={'form': form})


def user_logout(request):
    logout(request)
    return redirect('home:home')


def default(requset):
    return render(requset, 'accounts/Default.html')

# Create your views here.
