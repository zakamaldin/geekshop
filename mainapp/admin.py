from django.contrib import admin
from .models import ProductCategory, Product,Customer
# Register your models here.

admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(Customer)


