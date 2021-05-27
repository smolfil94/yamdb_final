from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination

from ..models import Genre
from ..permissions import IsAdminOrReadOnly
from ..serializers.genre_serializer import GenreSerializer
from .crd_view_set import CRDModelViewSet


class APIGenreViewSet(CRDModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter,)
    search_fields = ('name',)
    lookup_field = 'slug'
    permission_classes = [IsAdminOrReadOnly]
