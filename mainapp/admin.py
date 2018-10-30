from django.contrib import admin
from mainapp.models import ProductCategory, Product
from authapp.models import ShopUser
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ['image', 'name', 'category', 'short_desc', 'quantity', 'price']


admin.site.register(ProductCategory)
admin.site.register(Product, ProductAdmin)
admin.site.register(ShopUser)


