from django import forms
from django.contrib.auth.models import User
from .models import *

class UserRegisterForm(forms.Form):
    user_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={"placeholder" : "Enter Your Username"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder":"Enter Your Email"}))
    first_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={"placeholder":"Enter Your First Name"}))
    last_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={"placeholder":"Enter Your Last Name"}))
    password_1 = forms.CharField(max_length=50,widget=forms.PasswordInput(attrs={"placeholder":"Enter Your Password"}))
    password_2 = forms.CharField(max_length=50,widget=forms.PasswordInput(attrs={"placeholder":"Enter Your Password for Second Time"}))

    def clean_user_name(self):
        user = self.cleaned_data['user_name']
        if (User.objects.filter(username=user).exists()):
            raise forms.ValidationError('This Username already exists')
        return user

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('This email is submitted already \n Use an another one!')
        return email

    def clean_password_2(self):
        password1 = self.cleaned_data['password_1']
        password2 = self.cleaned_data['password_2']
        if password1 != password2:
            raise forms.ValidationError('Passwords arent match to each other')
        elif len(password2)<=8:
            raise  forms.ValidationError('Password is shorter than 8 character')
        elif not any(x.isupper() for x in password2):
            raise forms.ValidationError('Password must contains at least one upper character')
        return password1

class UserLoginForm(forms.Form):
    user_name = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email','first_name','last_name']


class LoginPhoneForm(forms.Form):
    phone = forms.IntegerField()

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone','address']


class CodeForm(forms.Form):
    code = forms.IntegerField()
