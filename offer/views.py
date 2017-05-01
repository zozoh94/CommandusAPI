from rest_framework import viewsets
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import LimitOffsetPagination

from .models import Offer
from .serializers import (OfferSerializer, OfferDetailSerializer)

class OfferViewSet(viewsets.ModelViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('restaurant',)
    pagination_class = LimitOffsetPagination
    def retrieve(self, request, pk=None):
        self.serializer_class = OfferDetailSerializer        
        return super(OfferViewSet, self).retrieve(request, pk)
