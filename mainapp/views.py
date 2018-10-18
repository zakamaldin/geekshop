from django.shortcuts import (
    render,
    get_list_or_404,
    get_object_or_404,
    redirect
)
from django.urls import reverse_lazy
from django.conf import settings
from mainapp.forms import ProductCategoryFormModel, ProductFormModel
from mainapp.models import Product, ProductCategory
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
    return render(request, 'mainapp/index.html', main_filling)


def product_info(request):
    return render(request, 'mainapp/product_info.html', product_info_filling)


def products(request):
    return render(request, 'mainapp/products.html', products_filling)


def contacts(request):
    return render(request, 'mainapp/contacts.html', {'contacts_filling': contacts_filling})


def product_category_create(request):
    template = 'mainapp/Lesson05.html'
    success_url = reverse_lazy()
    form = ProductCategoryFormModel(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return

# Lesson05 #


def product_list(request):
    query = get_list_or_404(Product)
    if request.method == 'POST':
        return redirect(reverse_lazy('mainapp:create'))
    return render(request, 'mainapp/product_list.html', {'results': query})


def product_detail(request, pk):
    obj = get_object_or_404(Product, pk=pk)
    form = ProductFormModel(instance=obj)
    template = 'mainapp/product_detail.html'
    content = {'form': form, 'button': 'edit'}
    if request.method == 'POST' and 'back' in request.POST:
        return redirect(reverse_lazy('mainapp:list'))

    if request.method == 'POST':
        return redirect(reverse_lazy('mainapp:product_edit', kwargs={'pk': pk}))

    return render(request, template, content)


def product_edit(request, pk):
    obj = get_object_or_404(Product, pk=pk)
    form = ProductFormModel(instance=obj)
    template = 'mainapp/product_detail.html'
    content = {'form': form, 'button': 'save', 'type': 'product_edit'}
    if request.method == 'POST' and 'back' in request.POST:
        return redirect(reverse_lazy('mainapp:list'))

    if request.method == 'POST' and 'delete' in request.POST:
        obj.delete()
        return redirect(reverse_lazy('mainapp:list'))

    if request.method == 'POST':
        form = ProductFormModel(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('mainapp:product_detail', kwargs={'pk': pk}))

    return render(request, template, content)


def product_create(request):
    form = ProductFormModel()
    template = 'mainapp/product_detail.html'
    content = {'form': form, 'button': 'add'}
    if request.method == 'POST' and 'back' in request.POST:
        return redirect(reverse_lazy('mainapp:list'))

    if request.method == 'POST':
        form = ProductFormModel(request.POST, request.FILES)
        if form.is_valid():
            print(request.FILES)
            form.save()
            return redirect(reverse_lazy('mainapp:list'))

    return render(request, template, content)

