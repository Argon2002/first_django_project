from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from random import randint
import ghasedakpack


def user_register(requset):
    if requset.method == 'POST':
        form = UserRegisterForm(requset.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(username=data["user_name"], email=data["email"], first_name=data["first_name"],
                                     last_name=data["last_name"], password=data["password_2"])
            user.save()
            messages.success(requset, "ثبت نام با موفقیت صورت گرفت", 'primary')
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
                messages.success(requset, "به سایت خوش آمدید", 'primary')
                return redirect('home:home')
            else:
                messages.success(requset, 'User or Password is wrong ', 'danger')

    else:
        form = UserLoginForm()

    return render(requset, 'accounts/Login.html', context={'form': form})


def user_logout(request):
    logout(request)
    messages.success(request, 'شما با موفقیت خارج شدید.', 'warning')
    return redirect('home:home')


@login_required(login_url='accounts:login')
def user_profile(request):
    profile = Profile.objects.get(user_id=request.user.id)
    return render(request, 'accounts/Profile.html', {'profile':profile})


@login_required(login_url='accounts:login')
def user_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST,instance=request.user)
        profile_form = ProfileUpdateForm(request.POST,instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,'update was successful','success')
            return redirect('accounts:profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {'user_form':user_form,'profile_form':profile_form}
    return  render(request,'accounts/Update.html',context)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            messages.success(request,'your password updated successfully \n test','success')
            return redirect('accounts:profile')
        else:
            messages.error(request,'No change','danger')
            return redirect('accounts:profile')
    else:
        form = PasswordChangeForm(request.user)
    return render(request,'accounts/ChangePassword.html',{'form':form})


def login_phone(request):
    if request.method == 'POST':
        form = LoginPhoneForm(request.POST)
        if form.is_valid():
            global random_code,phone
            data = form.cleaned_data
            phone = f"0{data['phone']}"
            random_code = randint(100,1000)
            sms = ghasedakpack.Ghasedak("d7bf5443d5246d766a6578b769565da8b4ceb469843c3e55716d68951ea7d5cd")
            print(random_code)
            sms.send({'message': f'  فروشگاه آرگون {random_code}', 'receptor': phone, 'linenumber': '3000xxxxx'})
            return redirect('accounts:login_phone_verify')

    else:
        form = LoginPhoneForm()
    return render(request,'accounts/LoginPhone.html',{'form':form})


def login_phone_verify(request):
    if request.method == 'POST':
        form = CodeForm(request.POST)
        if form.is_valid():
            if random_code == form.cleaned_data['code']:
                profile = Profile.objects.get(phone=phone)
                user = User.objects.get(profile__id = profile.id)
                login(request,user)
                messages.success(request,f'Welcome {user.username}')
                return redirect('home:home')
            else:
                messages.error(request,'code is wrong')
    else:
        form = CodeForm()
    return render(request,'accounts/LoginPhoneVerify.html', {'form': form})

def default(requset):
    return render(requset, 'accounts/Default.html')


