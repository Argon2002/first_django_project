from django.urls import  path
from . import  views

app_name= 'home'
urlpatterns = [
    path('',views.home,name='home'),
    path('product/',views.all_products,name='product'),
    path('argon/',views.argon,name='argon'),
    path('detail/<int:id>/',views.product_detail,name='product_detail'),
    path('category/<int:id>/',views.all_products,name='category'),

]