from rest_framework import serializers
from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)
from django.core.cache import cache
import json
from django.conf import settings
from urllib.request import urlopen

from .models import Dish, Restaurant

class RestaurantSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Restaurant
        fields = ('id', 'name', 'address', 'picture')

class DishSerializer(TaggitSerializer, serializers.ModelSerializer):
    ingredients = TagListSerializerField(required=False)
    restaurant_url = serializers.HyperlinkedRelatedField(view_name='restaurant-detail', read_only=True, source='restaurant')
    class Meta:
        model = Dish
        fields = ('id', 'url', 'name', 'ingredients', 'price', 'picture', 'restaurant_url')

class IngredientsSerializer(serializers.BaseSerializer):
    def to_representation(self, obj):
        ingredients = []
        for ingredient in obj.names():
            if cache.get(ingredient) is not None:
                ingredients.append({'name': ingredient, 'picture': cache.get(ingredient)})                
            else:                
                picture = None
                serialized_data = urlopen(settings.PIXABAY_API_URL+'?key='+settings.PIXABAY_API_KEY
                                          +'&q='+ingredient+'&per_page=3&safesearch=true&image_type=photo'
                                          +'&lang=fr').read().decode('utf-8')           
                data = json.loads(serialized_data)
                if data['hits']:
                    picture = data['hits'][0]['webformatURL']
                    cache.set(ingredient, picture, None)
                else:
                    cache.set(ingredient, picture, 1296000) 
                ingredients.append({'name': ingredient, 'picture': picture})
        return ingredients
        
class DishDetailSerializer(DishSerializer):
    restaurant_detail = RestaurantSerializer(read_only=True, source='restaurant')
    ingredients_with_pictures = IngredientsSerializer(read_only=True, source='ingredients')
    class Meta:
        model = Dish
        fields = ('id', 'name', 'ingredients_with_pictures', 'duration', 'price', 'picture', 'restaurant_detail', 'categories')
