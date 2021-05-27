from django.shortcuts import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

from ..models.title import Title
from ..permissions import IsModeratorOrAdminOrAuthorOrReadOnly
from ..serializers.review_serializer import ReviewSerializer


class APIReviewViewSet(ModelViewSet):
    pagination_class = PageNumberPagination
    permission_classes = [IsModeratorOrAdminOrAuthorOrReadOnly]
    serializer_class = ReviewSerializer

    def get_queryset(self):
        title = get_object_or_404(Title, pk=self.kwargs.get('title_id'))
        return title.reviews.all()

    def perform_create(self, serializer):
        title = get_object_or_404(Title, pk=self.kwargs.get('title_id'))
        serializer.save(author=self.request.user, title=title)
