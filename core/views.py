from rest_framework import viewsets
from rest_framework import permissions

from .models import Dish, Restaurant
from .serializers import DishSerializer, DishDetailSerializer, RestaurantSerializer, RestaurantDetailSerializer

class DishViewSet(viewsets.ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)    
    def retrieve(self, request, pk=None):
        self.serializer_class = DishDetailSerializer        
        return super(DishViewSet, self).retrieve(request, pk)

class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)
    def retrieve(self, request, pk=None):
        self.serializer_class = RestaurantDetailSerializer        
        return super(RestaurantViewSet, self).retrieve(request, pk)
