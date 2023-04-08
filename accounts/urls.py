from django.urls import  path
from . import  views


app_name= 'accounts'
urlpatterns = [
    path('',views.default,name='default'),
    path('register/',views.user_register,name='user_register'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('profile/',views.user_profile,name='profile'),
    path('update/',views.user_update,name='update'),
    path('change_password/',views.change_password,name='change_password'),
    path('login_phone/',views.login_phone,name='login_phone'),
    path('login_phone_verify/',views.login_phone_verify,name='login_phone_verify')


]