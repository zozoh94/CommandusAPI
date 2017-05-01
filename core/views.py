from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import detail_route
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import LimitOffsetPagination

from .models import Dish, Restaurant, Menu, Category, Review
from .serializers import (DishSerializer, DishDetailSerializer,
                          RestaurantSerializer, RestaurantDetailSerializer,
                          MenuSerializer, MenuDetailSerializer,
                          CategorySerializer, CategoryDetailSerializer,
                          ReviewSerializer, ReviewDetailSerializer)

class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)
    pagination_class = LimitOffsetPagination
    def retrieve(self, request, pk=None):        
        self.serializer_class = RestaurantDetailSerializer        
        return super(RestaurantViewSet, self).retrieve(request, pk)

class DishViewSet(viewsets.ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('categories', 'menus', 'restaurant')
    pagination_class = LimitOffsetPagination
    def retrieve(self, request, pk=None):
        self.serializer_class = DishDetailSerializer        
        return super(DishViewSet, self).retrieve(request, pk)
   
class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('restaurant',)
    pagination_class = LimitOffsetPagination
    def retrieve(self, request, pk=None):
        self.serializer_class = MenuDetailSerializer        
        return super(MenuViewSet, self).retrieve(request, pk)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('menus', 'restaurant')
    pagination_class = LimitOffsetPagination
    def retrieve(self, request, pk=None):
        self.serializer_class = CategoryDetailSerializer        
        return super(CategoryViewSet, self).retrieve(request, pk)

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('restaurant',)
    pagination_class = LimitOffsetPagination
    def retrieve(self, request, pk=None):
        self.serializer_class = ReviewDetailSerializer        
        return super(ReviewViewSet, self).retrieve(request, pk)
