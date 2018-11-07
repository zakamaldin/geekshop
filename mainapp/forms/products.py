from django import forms
from mainapp.models import Product


class ProductFormModel(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['image', 'name', 'category', 'short_desc', 'description', 'quantity', 'price']
