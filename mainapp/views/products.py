from django.shortcuts import (
    render,
    get_list_or_404,
    get_object_or_404,
    redirect
)
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.views.generic.edit import FormMixin
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
    form_class = ProductFormModel
    success_url = reverse_lazy('products:product_list')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['button'] = 'Add'
        return context


class ProductDetailView(FormMixin, DetailView):
    model = Product
    template_name = 'mainapp/product_detail.html'
    form_class = ProductFormModel

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['form'] = ProductFormModel(instance=self.object)
        context['button'] = 'Edit'
        context['type'] = 'detail'

        return context


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'mainapp/product_detail.html'
    form_class = ProductFormModel
    success_url = reverse_lazy('products:product_list')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ProductUpdateView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['form'] = ProductFormModel(instance=self.object)
        context['button'] = 'Save'
        context['type'] = 'edit'
        return context


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'mainapp/product_detail.html'
    form_class = ProductFormModel
    success_url = reverse_lazy('products:product_list')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ProductDeleteView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['form'] = ProductFormModel(instance=self.object)
        context['button'] = 'Yes, delete'
        context['type'] = 'delete'
        return context

