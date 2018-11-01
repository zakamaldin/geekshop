from django.contrib import admin
from mainapp.models import ProductCategory, Product
from authapp.models import ShopUser
from django.utils.timezone import now, timedelta
from django.template.loader import render_to_string
# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'picture',
        'name',
        'is_new',
        'is_active',
        'category',
        'short_desc',
        'quantity',
        'price',
        'created',
        'modified',
    ]

    list_filter = [
        'category',
        'created',
        'modified',
    ]

    search_fields = [
        'name',
        'short_desc',
        'quantity',
        'price',

    ]

    fieldsets = [
        (
            None, {
                'fields': (
                    'name',
                    'category'
                )
            }
        ),
        (
            'Content', {
                'fields': (
                    'image',
                    'short_desc',
                    'description',
                    'quantity',
                    'price'
                )
            }
        ),

    ]

    def picture(self, obj):
        return render_to_string(
            'components/picture.html',
            {'image': obj.image.url}

        )

    def is_new(self, obj):
        return obj.created >= (now() - timedelta(days=5))

    is_new.boolean = True


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'description',
        'is_new',
        'is_active',
        'created',
        'modified',
    ]

    list_filter = [
        'description'
    ]

    search_fields = [
        'description'

    ]

    fieldsets = [
        (
            None, {
                'fields': (
                    'name',
                    'description'
                )
            }
        )

    ]

    def is_new(self, obj):
        return obj.created >= (now() - timedelta(days=5))

    is_new.boolean = True


admin.site.register(ShopUser)


