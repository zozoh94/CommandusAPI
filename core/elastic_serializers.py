from rest_framework_elasticsearch.es_serializer import ElasticModelSerializer
from rest_framework import serializers
from .models import Restaurant
from .elastic_index import RestaurantIndex

class ElasticRestaurantSerializer(ElasticModelSerializer):
    class Meta:
        model = Restaurant
        es_model = RestaurantIndex
        fields = ('pk', 'name', 'address', 'location')
