from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views.api_category_view_set import APICategoryViewSet
from api.views.api_comment_view_set import APICommentViewSet
from api.views.api_genre_view_set import APIGenreViewSet
from api.views.api_review_view_set import APIReviewViewSet
from api.views.api_title_view_set import APITitleViewSet

router_v1 = DefaultRouter()

router_v1.register('titles', APITitleViewSet)
router_v1.register('genres', APIGenreViewSet)
router_v1.register('categories', APICategoryViewSet)
router_v1.register(r'titles/(?P<title_id>\d+)/reviews', APIReviewViewSet,
                   basename='Review')
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    APICommentViewSet
)

urlpatterns = [
    path('v1/', include(router_v1.urls)),
]
