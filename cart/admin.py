from django.contrib import admin
from .models import Order, OrderItem
# Register your models here.


class OrderItemInline(admin.TabularInline):
    model = OrderItem


class OrderModelAdmin(admin.ModelAdmin):
    list_display = ['user', 'is_active', 'created']
    inlines = [OrderItemInline]

admin.site.register(Order, OrderModelAdmin)
admin.site.register(OrderItem)

