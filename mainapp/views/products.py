from django.shortcuts import (
    render,
    get_list_or_404,
    get_object_or_404,
    redirect
)
from django.views.generic import (
    ListView, DetailView, CreateView
)
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.conf import settings
import json
import os
from mainapp.forms import ProductFormModel
from mainapp.models import Product


path_to_json            = os.path.join(settings.BASE_DIR, 'mainapp/static/mainapp/json')
main_filling            = json.load(open(os.path.join(path_to_json, 'main.json'), 'r'))
products_filling        = json.load(open(os.path.join(path_to_json, 'products.json'), 'r'))
product_info_filling    = json.load(open(os.path.join(path_to_json, 'product_info.json'), 'r'))
contacts_filling        = json.load(open(os.path.join(path_to_json, 'contacts.json'), 'r'))


def main(request):
    return render(request, 'mainapp/index.html', main_filling)


def product_info(request):
    return render(request, 'mainapp/product_info.html', product_info_filling)


def products(request):
    return render(request, 'mainapp/products.html', products_filling)


def contacts(request):
    return render(request, 'mainapp/contacts.html', {'contacts_filling': contacts_filling})

# Lesson06 #


class ProductListView(ListView):
    model = Product
    template_name = 'mainapp/product_list.html'
    context_object_name = 'results'
    paginate_by = 3


class ProductCreateView(CreateView):
    model = Product
    template_name = 'mainapp/product_detail.html'
    context_object_name = 'form'
    form_class = ProductFormModel
    success_url = reverse_lazy('products:product_list')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['button'] = 'add'
        return context


def product_detail(request, pk):
    obj = get_object_or_404(Product, pk=pk)
    form = ProductFormModel(instance=obj)
    template = 'mainapp/product_detail.html'
    content = {'form': form, 'button': 'edit'}
    success_url = 'products:product_list'
    if request.method == 'POST' and 'back' in request.POST:
        return redirect(reverse_lazy(success_url))

    if request.method == 'POST':
        return redirect(reverse_lazy('products:product_edit', kwargs={'pk': pk}))

    return render(request, template, content)


def product_edit(request, pk):
    obj = get_object_or_404(Product, pk=pk)
    form = ProductFormModel(instance=obj)
    template = 'mainapp/product_detail.html'
    content = {'form': form, 'button': 'save', 'type': 'edit'}
    success_url = 'products:product_list'
    if request.method == 'POST' and 'back' in request.POST:
        return redirect(reverse_lazy(success_url))

    if request.method == 'POST' and 'delete' in request.POST:
        obj.delete()
        return redirect(reverse_lazy(success_url))

    if request.method == 'POST':
        form = ProductFormModel(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('products:product_detail', kwargs={'pk': pk}))

    return render(request, template, content)


