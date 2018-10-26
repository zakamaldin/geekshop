from django.shortcuts import (
    get_list_or_404,
)

from mainapp.models import Product
from django.http import JsonResponse


def rest_product_list(request):
    query = get_list_or_404(Product)
    data = map(
        lambda itm: {
            'category': itm.category.name,
            'name': itm.name,
            #'image': itm.image,
            'short_desc': itm.short_desc,
            'description': itm.description,
            'price': itm.price,
            'quantity': itm.quantity

        },
        query
    )
    return JsonResponse(
        {
            'results': list(data)
        },
    )