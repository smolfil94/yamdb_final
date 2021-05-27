from rest_framework.mixins import (CreateModelMixin, DestroyModelMixin,
                                   ListModelMixin)
from rest_framework.viewsets import GenericViewSet


class CRDModelViewSet(CreateModelMixin,
                      ListModelMixin,
                      DestroyModelMixin,
                      GenericViewSet):
    """
    A viewset that provides default `create()`, `list()` and
    'destroy()' actions.
    """

    pass
