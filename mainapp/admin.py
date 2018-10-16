from django.contrib import admin
from mainapp.models import ProductCategory, Product, Customer
from authapp.models import ShopUser
# Register your models here.

admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(ShopUser)


