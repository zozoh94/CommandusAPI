from rest_framework import serializers
from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)

from .models import (Dish, Restaurant)

class RestaurantSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Restaurant
        fields = ('id', 'name', 'address')

class DishSerializer(TaggitSerializer, serializers.ModelSerializer):
    ingredients = TagListSerializerField(required=False)
    restaurant_url = serializers.HyperlinkedRelatedField(view_name='restaurant-detail', read_only=True, source='restaurant')
    class Meta:
        model = Dish
        fields = ('id', 'url', 'name', 'ingredients', 'price', 'picture', 'restaurant_url')

class DishDetailSerializer(DishSerializer):
    restaurant_detail = RestaurantSerializer(read_only=True, source='restaurant')
    class Meta:
        model = Dish
        fields = ('id', 'name', 'ingredients_with_pictures', 'duration', 'price', 'picture', 'restaurant_detail')
