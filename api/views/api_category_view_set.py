from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination

from ..models import Category
from ..permissions import IsAdminOrReadOnly
from ..serializers.category_serializer import CategorySerializer
from .crd_view_set import CRDModelViewSet


class APICategoryViewSet(CRDModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter,)
    search_fields = ('name',)
    lookup_field = 'slug'
    permission_classes = [IsAdminOrReadOnly]
