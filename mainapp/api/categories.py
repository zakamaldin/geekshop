from django.shortcuts import (
    get_list_or_404,
)

from mainapp.models import ProductCategory
from django.http import JsonResponse


def rest_category_list(request):
    query = get_list_or_404(ProductCategory)
    data = map(
        lambda itm: {
            'title': itm.name,
            'description': itm.description,
        },
        query
    )
    return JsonResponse(
        {
            'results': list(data)
        }
    )
