from django import forms
from mainapp.models import ProductCategory


class ProductCategoryFormModel(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = ['name', 'description']
