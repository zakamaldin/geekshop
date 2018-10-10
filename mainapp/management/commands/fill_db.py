from django.core.management.base import BaseCommand
from mainapp.models import Product, ProductCategory
from django.conf import settings


import json
import os

JSON_PATH = os.path.join(settings.BASE_DIR, 'mainapp/static/db/json')


def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r', encoding='utf-8') as infile:
        return json.load(infile)


class Command(BaseCommand):

    def handle(self, *args, **options):
        categories = load_from_json('categories')
        ProductCategory.objects.all().delete()
        for c in categories:
            new_category = ProductCategory(**c)
            new_category.save()

        products = load_from_json('products')
        Product.objects.all().delete()
        for p in products:
            category_name = p['category']
            category = ProductCategory.objects.get(name=category_name)
            p['category'] = category
            new_product = Product(**p)
            new_product.save()

