from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.views.generic.edit import FormMixin
from django.urls import reverse_lazy
from mainapp.forms import ProductCategoryFormModel
from mainapp.models import ProductCategory


class ProductCategoryListView(ListView):
    queryset = ProductCategory.objects.filter(is_active=True)
    template_name = 'mainapp/category_list.html'
    context_object_name = 'results'
    paginate_by = 3


class ProductCategoryCreateView(LoginRequiredMixin, CreateView):
    model = ProductCategory
    template_name = 'mainapp/category_detail.html'
    form_class = ProductCategoryFormModel
    success_url = reverse_lazy('categories:category_list')
    login_url = reverse_lazy('auth:login')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['button'] = 'Add'
        context['type'] = 'create'
        return context


class ProductCategoryDetailView(FormMixin, DetailView):
    queryset = ProductCategory.objects.filter(is_active=True)
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


class ProductCategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = ProductCategory
    template_name = 'mainapp/category_detail.html'
    form_class = ProductCategoryFormModel
    success_url = reverse_lazy('categories:category_list')
    login_url = reverse_lazy('auth:login')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ProductCategoryUpdateView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['form'] = ProductCategoryFormModel(instance=self.object)
        context['button'] = 'Save'
        context['type'] = 'edit'
        return context


class ProductCategoryDeleteView(DeleteView):
    queryset = ProductCategory.objects.filter(is_active=True)
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

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

