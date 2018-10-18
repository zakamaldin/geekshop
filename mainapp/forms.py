from django import forms
from mainapp.models import (
    ProductCategory,
    Product
)


class ProductCategoryFormModel(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = ['name', 'description']


class ProductFormModel(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['image', 'name', 'category', 'short_desc', 'description', 'quantity', 'price']
