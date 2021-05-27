from django.conf.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import ConfirmCodeView, TokenView, UserViewSet

router_v1 = DefaultRouter()
router_v1.register('users', UserViewSet, basename='users')

registration = [
    path('email/', ConfirmCodeView.as_view(), name='sent_confirm_code'),
    path('token/', TokenView.as_view(), name='sent_jwt_token'),
]

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/auth/', include(registration)),
]
