from django.shortcuts import render


def main(request):
    return render(request, 'mainapp/index.html')


def product_info(request):
    return render(request, 'mainapp/product.html')


def products(request):
    return render(request, 'mainapp/products.html')


def contacts(request):
    return render(request, 'mainapp/contacts.html')
