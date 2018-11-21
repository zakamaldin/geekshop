from django.shortcuts import (
    render,
)
from django.http import HttpResponseRedirect

from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.views.generic.edit import FormMixin
from django.urls import reverse_lazy
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin

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
    queryset = Product.objects.filter(is_active=True)
    template_name = 'mainapp/product_list.html'
    context_object_name = 'results'
    paginate_by = 3


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    template_name = 'mainapp/product_detail.html'
    form_class = ProductFormModel
    success_url = reverse_lazy('products:product_list')
    login_url = reverse_lazy('auth:login')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['button'] = 'Add'
        context['type'] = 'create'
        return context


class ProductDetailView(FormMixin, DetailView):
    queryset = Product.objects.filter(is_active=True)
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


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    template_name = 'mainapp/product_detail.html'
    form_class = ProductFormModel
    success_url = reverse_lazy('products:product_list')
    login_url = reverse_lazy('auth:login')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ProductUpdateView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['form'] = ProductFormModel(instance=self.object)
        context['button'] = 'Save'
        context['type'] = 'edit'
        return context


class ProductDeleteView(DeleteView):
    queryset = Product.objects.filter(is_active=True)
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

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())



