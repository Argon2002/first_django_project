from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','create','update')
    list_filter = ('create',)


admin.site.register(Category,CategoryAdmin)

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name','amount','product_price','discount','total_price','available','create','update',)
    list_filter = ('name','amount','create','available')

admin.site.register(Product,ProductsAdmin)

