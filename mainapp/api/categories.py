from mainapp.models import ProductCategory
from django.http import JsonResponse
from django.views.generic import ListView
from django.urls import reverse

from rest_framework.viewsets import ModelViewSet
from mainapp.serializer import ProductCategorySerializer


class ProductCategoryViewSet(ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer


class CategoryList(ListView):
    model = ProductCategory
    paginate_by = 3

    def serialize_object_list(self, queryset):
        return list(
            map(
                lambda itm: {
                    'title': itm.name,
                    'description': itm.description,
                    'modified': itm.modified,
                    'created': itm.created,
                },
                queryset
            )
        )

    def get_context_data(self, **kwargs):
        context = super(CategoryList, self).get_context_data(**kwargs)

        data = {}
        page = context.get('page_obj')
        route_url = reverse('rest_categories:rest_list')
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
