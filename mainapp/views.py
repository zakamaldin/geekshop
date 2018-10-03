from django.shortcuts import render
from django.conf import settings
from .models import ProductCategory, Product
import json
import os
path_to_json            = os.path.join(settings.BASE_DIR, 'mainapp/static/mainapp/json')
main_filling            = json.load(open(os.path.join(path_to_json, 'main.json'), 'r'))
products_filling        = json.load(open(os.path.join(path_to_json, 'products.json'), 'r'))
product_info_filling    = json.load(open(os.path.join(path_to_json, 'product_info.json'), 'r'))
contacts_filling        = json.load(open(os.path.join(path_to_json, 'contacts.json'), 'r'))


def main(request):
    title = 'Lesson03'
    products = Product.objects.all()[:4]
    content = {'title': title, 'products': products}
    #return render(request, 'mainapp/index.html', main_filling)
    return render(request, 'mainapp/Lesson03.html', content)


def product_info(request):
    return render(request, 'mainapp/product_info.html', product_info_filling)


def products(request):
    return render(request, 'mainapp/products.html', products_filling)


def contacts(request):
    return render(request, 'mainapp/contacts.html', {'contacts_filling': contacts_filling})
