from rest_framework import serializers
from mainapp.models import Product, ProductCategory


class ProductSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            'url',
            'image',
            'name',
            'category',
            'short_desc',
            'description',
            'quantity',
            'price',
            'modified',
            'created',
        ]

    def get_image(self, obj):
        return obj.image.url

    def get_category(self, obj):
        return obj.category.name


class ProductCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductCategory
        fields = [
            'url',
            'name',
            'description',
            'modified',
            'created',
        ]


