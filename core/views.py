from rest_framework import viewsets
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.decorators import list_route
from rest_framework import status

from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search
from elasticsearch_dsl.query import MultiMatch, Q

from .models import Dish, Restaurant, Menu, Category, Review, Schedule
from .serializers import (DishSerializer, DishDetailSerializer,
                          RestaurantSerializer, RestaurantDetailSerializer,
                          MenuSerializer, MenuDetailSerializer,
                          CategorySerializer, CategoryDetailSerializer,
                          ReviewSerializer, ReviewDetailSerializer,
                          ScheduleSerializer, ScheduleDetailSerializer)

class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)
    pagination_class = LimitOffsetPagination
    def retrieve(self, request, pk=None):        
        self.serializer_class = RestaurantDetailSerializer        
        return super(RestaurantViewSet, self).retrieve(request, pk)
    @list_route()
    def search(self, request):
        lat = request.query_params.get('lat', None)
        lon = request.query_params.get('lon', None)
        distance = request.query_params.get('distance', '10km')
        q = request.query_params.get('q', None)
        client = Elasticsearch()
        s = Search(using=client, index="commandus", doc_type="restaurant_index")
        if lat and lon:
            s = s.filter('geo_distance', distance=distance, location={'lat': lat, 'lon': lon})
        if q:
            q = Q('bool',
                  must=[Q('bool',
                          should=[Q('simple_query_string', query=q, fields=['_all']),
                          MultiMatch(query=q, type='phrase_prefix', fields=['name^2', 'address'])]                     
                  )],
            )
            s = s.query(q)
        response = s.execute()
        restaurants_ids = [hit.pk for hit in response.hits]
        self.queryset = Restaurant.objects.filter(id__in=[hit.pk for hit in response.hits])
        return super(RestaurantViewSet, self).list(request)
        
    
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

class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('restaurant', 'day')
    pagination_class = LimitOffsetPagination
    def retrieve(self, request, pk=None):
        self.serializer_class = ScheduleDetailSerializer        
        return super(ScheduleViewSet, self).retrieve(request, pk)
    
