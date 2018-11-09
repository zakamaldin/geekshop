from mainapp.models import Product
from django.http import JsonResponse
from django.views.generic import ListView
from django.urls import reverse

from rest_framework.viewsets import ModelViewSet
from mainapp.serializer import ProductSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductList(ListView):
    model = Product
    paginate_by = 3

    def serialize_object_list(self, queryset):
        return list(
            map(
                lambda itm: {
                    'category': itm.category.name,
                    'name': itm.name,
                    'image': itm.image.url,
                    'short_desc': itm.short_desc,
                    'description': itm.description,
                    'price': itm.price,
                    'quantity': itm.quantity,
                    'modified': itm.modified,
                    'created': itm.created,
                },
                queryset
            )
        )

    def get_context_data(self, **kwargs):
        context = super(ProductList, self).get_context_data(**kwargs)

        data = {}
        page = context.get('page_obj')
        route_url = reverse('rest_products:rest_list')
        data['next_page'] = None
        data['previous_page'] = None
        data['page'] = page.number
        data['count'] = page.paginator.count
        data['results'] = self.serialize_object_list(page.object_list)

        if page.has_next():
            data['next_page'] = f'{route_url}?page={page.next_page_number()}'

        if page.has_previous():
            data['previous_page'] = f'{route_url}?page={page.previous_page_number()}'

        return data

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(context)
