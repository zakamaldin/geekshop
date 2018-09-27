from django.shortcuts import render

main_filling = {
    'content': {
        'img_src': ['product-1.jpg', 'product-2.jpg', 'product-3.jpg', 'product-4.jpg'],
        'h3': 'Fishnet Chair',
        'p': 'Seat and back with upholstery made of cold cure foam'},
    'trends': {
        'img_src': ['trend-1.jpg', 'trend-2.jpg', 'trend-3.jpg', 'trend-4.jpg', 'trend-5.jpg', 'trend-6.jpg'],
        'h2': 'Fishnet Chair',
        'p': 'Seat and back with upholstery made of cold cure foam. Steel frame,'
             ' available in matt powder-coated black'},
    'exclusive': {
        'img_src': ['exclusive-1.jpg', 'exclusive-2.jpg', 'exclusive-3.jpg', 'exclusive-4.jpg'],
        'h3': 'Fishnet Chair',
        'p': 'Seat and back with upholstery made of cold cure foam'},
    'slider1': {
        'h3': 'TRENDING',
        'h2': 'Fishnet Chair',
        'p': 'Seat and back with upholstery made of cold cure foam. Steel frame, available in matt powder-coated black'},
    'slider2': {
        'h3': 'HOT DEAL',
        'h2': 'Fishnet Chair',
        'p': 'Seat and back with upholstery made of cold cure foam. Steel frame, available in matt powder-coated black'},
}


def main(request):
    return render(request, 'mainapp/index_test_templates.html', main_filling)


def product_info(request):
    return render(request, 'mainapp/product.html')


def products(request):
    return render(request, 'mainapp/products.html')


def contacts(request):
    return render(request, 'mainapp/contacts.html')
