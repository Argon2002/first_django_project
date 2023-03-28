from django.urls import  path
from . import  views

app_name= 'accounts'
urlpatterns = [
    path('',views.default,name='default'),
    path('register/',views.user_register,name='user_register'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout')


]