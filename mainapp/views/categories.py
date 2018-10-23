from django.shortcuts import (
    render,
    get_list_or_404,
    get_object_or_404,
    redirect
)
from django.urls import reverse_lazy
from mainapp.forms import ProductCategoryFormModel
from mainapp.models import ProductCategory


def category_list(request):
    query = get_list_or_404(ProductCategory)
    if request.method == 'POST':
        return redirect(reverse_lazy('categories:category_create'))
    return render(request, 'mainapp/category_list.html', {'results': query})


def category_detail(request, pk):
    obj = get_object_or_404(ProductCategory, pk=pk)
    form = ProductCategoryFormModel(instance=obj)
    template = 'mainapp/category_detail.html'
    content = {'form': form, 'button': 'edit'}
    success_url = 'categories:category_list'
    if request.method == 'POST' and 'back' in request.POST:
        return redirect(reverse_lazy(success_url))

    if request.method == 'POST':
        return redirect(reverse_lazy('categories:category_edit', kwargs={'pk': pk}))

    return render(request, template, content)


def category_create(request):
    form = ProductCategoryFormModel()
    template = 'mainapp/category_detail.html'
    content = {'form': form, 'button': 'add'}
    success_url = 'categories:category_list'
    if request.method == 'POST' and 'back' in request.POST:
        return redirect(reverse_lazy(success_url))

    if request.method == 'POST':
        form = ProductCategoryFormModel(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy(success_url))

    return render(request, template, content)


def category_edit(request, pk):
    obj = get_object_or_404(ProductCategory, pk=pk)
    form = ProductCategoryFormModel(instance=obj)
    template = 'mainapp/category_detail.html'
    content = {'form': form, 'button': 'save', 'type': 'edit'}
    success_url = 'categories:category_list'
    if request.method == 'POST' and 'back' in request.POST:
        return redirect(reverse_lazy(success_url))

    if request.method == 'POST' and 'delete' in request.POST:
        obj.delete()
        return redirect(reverse_lazy(success_url))

    if request.method == 'POST':
        form = ProductCategoryFormModel(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('categories:category_detail', kwargs={'pk': pk}))

    return render(request, template, content)

