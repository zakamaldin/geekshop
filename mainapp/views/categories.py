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
from django.urls import reverse_lazy
from mainapp.forms import ProductCategoryFormModel
from mainapp.models import ProductCategory


class ProductCategoryListView(ListView):
    model = ProductCategory
    template_name = 'mainapp/category_list.html'
    context_object_name = 'results'
    paginate_by = 3


class ProductCategoryCreateView(CreateView):
    model = ProductCategory
    template_name = 'mainapp/category_detail.html'
    form_class = ProductCategoryFormModel
    success_url = reverse_lazy('categories:category_list')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['button'] = 'Add'
        return context


class ProductCategoryDetailView(FormMixin, DetailView):
    model = ProductCategory
    template_name = 'mainapp/category_detail.html'
    form_class = ProductCategoryFormModel

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ProductCategoryDetailView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['form'] = ProductCategoryFormModel(instance=self.object)
        context['button'] = 'Edit'
        context['type'] = 'detail'

        return context


class ProductCategoryUpdateView(UpdateView):
    model = ProductCategory
    template_name = 'mainapp/category_detail.html'
    form_class = ProductCategoryFormModel
    success_url = reverse_lazy('categories:category_list')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ProductCategoryUpdateView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['form'] = ProductCategoryFormModel(instance=self.object)
        context['button'] = 'Save'
        context['type'] = 'edit'
        return context


class ProductCategoryDeleteView(DeleteView):
    model = ProductCategory
    template_name = 'mainapp/category_detail.html'
    form_class = ProductCategoryFormModel
    success_url = reverse_lazy('categories:category_list')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ProductCategoryDeleteView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['form'] = ProductCategoryFormModel(instance=self.object)
        context['button'] = 'Yes, delete'
        context['type'] = 'delete'
        return context



