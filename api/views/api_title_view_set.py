from django.db.models import Avg
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import SAFE_METHODS
from rest_framework.viewsets import ModelViewSet

from ..filter import TitleFilter
from ..models import Title
from ..permissions import IsAdminOrReadOnly
from ..serializers.title_serializer import (GetTitleSerializer,
                                            PostTitleSerializer,
                                            TitleSerializer)


class APITitleViewSet(ModelViewSet):
    queryset = (Title.objects.annotate(rating=Avg('reviews__score'))
                .order_by('-rating'))
    serializer_class = TitleSerializer
    pagination_class = PageNumberPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TitleFilter
    permission_classes = [IsAdminOrReadOnly]

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return GetTitleSerializer
        return PostTitleSerializer
