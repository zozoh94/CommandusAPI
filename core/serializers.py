from rest_framework import serializers
from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)
from django.core.cache import cache
import json
from django.conf import settings
from urllib.request import urlopen

from .models import Dish, Restaurant, Menu, Review, Category, Schedule, ScheduleTime
from .models import NumberCategoryMenu, NumberDishMenu
from offer.models import Offer

class OfferSerializer(serializers.RelatedField):
    def to_representation(self, value):    
        return (value.name + ('(' + value.description + ') ' if value.description else ''))

# RESTAURANT

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('id', 'url', 'name', 'address', 'picture')

class ScheduleTimeInRestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduleTime
        fields = ('opening_time', 'closing_time')
        
class ScheduleInRestaurantSerializer(serializers.ModelSerializer):
    times = ScheduleTimeInRestaurantSerializer(many=True, read_only=True)
    class Meta:
        model = Schedule
        fields = ('day', 'times')
    
class RestaurantInSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('url', 'name', 'address', 'picture')
        
class ReviewInRestaurantSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username') 
    class Meta:
        model = Review
        fields = ('id', 'url', 'note', 'description', 'author')
        
class DishInRestaurantSerializer(serializers.ModelSerializer):
    ingredients = TagListSerializerField(required=False)
    class Meta:
        model = Dish
        fields = ('id', 'url', 'name', 'ingredients', 'price', 'picture')

class MenuInRestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ('id', 'url', 'name', 'price', 'description')
        
class RestaurantDetailSerializer(serializers.ModelSerializer):
    offers = OfferSerializer(many=True, read_only=True)
    menus = MenuInRestaurantSerializer(many=True, read_only=True)
    reviews = ReviewInRestaurantSerializer(many=True, read_only=True)
    dishes = DishInRestaurantSerializer(many=True, read_only=True)
    schedules = ScheduleInRestaurantSerializer(many=True, read_only=True)
    class Meta:
        model = Restaurant
        fields = ('id', 'name', 'address', 'picture',
                  'menus', 'offers', 'reviews', 'dishes',
                  'schedules', 'open')


# DISH
        
class DishSerializer(TaggitSerializer, serializers.ModelSerializer):
    ingredients = TagListSerializerField(required=False)
    restaurant_url = serializers.HyperlinkedRelatedField(view_name='restaurant-detail',
                                                         read_only=True, source='restaurant')
    class Meta:
        model = Dish
        fields = ('id', 'url', 'name', 'ingredients', 'price', 'picture',
                  'restaurant_url')

class IngredientsSerializer(serializers.BaseSerializer):
    def to_representation(self, obj):
        ingredients = []
        for ingredient in obj.names():
            if cache.get(ingredient) is not None:
                ingredients.append({'name': ingredient, 'picture': cache.get(ingredient)})                
            else:                
                picture = None
                try:
                    serialized_data = urlopen(settings.PIXABAY_API_URL+'?key='+settings.PIXABAY_API_KEY
                                              +'&q='+ingredient+'&per_page=3&safesearch=true&image_type=photo'
                                              +'&lang=fr').read().decode('utf-8')           
                    data = json.loads(serialized_data)
                    if data['hits']:
                        picture = data['hits'][0]['webformatURL']
                        cache.set(ingredient, picture, None)
                    else:
                        cache.set(ingredient, picture, 1296000)
                except:
                    pass
                ingredients.append({'name': ingredient, 'picture': picture})
        return ingredients

class CategoryInDishSerializer(serializers.ModelSerializer):
    def to_representation(self, obj):
        return obj.name
    class Meta:
        model = Category

class MenuInDishSerializer(serializers.ModelSerializer):
    offers = OfferSerializer(many=True, read_only=True)
    class Meta:
        model = Menu
        fields = ('id', 'url', 'name', 'price', 'description', 'offers')
        
class DishDetailSerializer(serializers.ModelSerializer):
    restaurant_detail = RestaurantInSerializer(read_only=True, source='restaurant')
    ingredients_with_pictures = IngredientsSerializer(read_only=True, source='ingredients')
    menus = MenuInDishSerializer(many=True, read_only=True)
    categories = CategoryInDishSerializer(many=True)
    offers = OfferSerializer(many=True, read_only=True)
    class Meta:
        model = Dish
        fields = ('id', 'name', 'ingredients_with_pictures', 'duration', 'price', 'picture',
                  'restaurant', 'restaurant_detail', 'categories', 'menus', 'offers')


# CATEGORY

class CategorySerializer(serializers.ModelSerializer):
    restaurant_url = serializers.HyperlinkedRelatedField(view_name='restaurant-detail',
                                                         read_only=True, source='restaurant')
    class Meta:
        model = Category
        fields = ('id', 'url', 'name', 'restaurant_url')

class MenuInCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ('id', 'url', 'name', 'price', 'description')

class DishInCategorySerializer(serializers.ModelSerializer):
    ingredients = TagListSerializerField(required=False)
    class Meta:
        model = Dish
        fields = ('id', 'url', 'name', 'ingredients', 'price', 'picture')

class CategoryDetailSerializer(serializers.ModelSerializer):
    restaurant_detail = RestaurantInSerializer(read_only=True, source='restaurant')
    menus = MenuInCategorySerializer(many=True, read_only=True)
    dishes = DishInCategorySerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ('id', 'name', 'restaurant', 'restaurant_detail', 'menus', 'dishes')

        
# REVIEW
        
class ReviewSerializer(serializers.ModelSerializer):
    restaurant_url = serializers.HyperlinkedRelatedField(view_name='restaurant-detail',
                                                         read_only=True, source='restaurant')
    author = serializers.ReadOnlyField(source='author.username') 
    class Meta:
        model = Review
        fields = ('id', 'url', 'description', 'note', 'author', 'restaurant_url')

class ReviewDetailSerializer(serializers.ModelSerializer):
    restaurant_detail = RestaurantInSerializer(read_only=True, source='restaurant')
    author_username = serializers.ReadOnlyField(source='author.username') 
    class Meta:
        model = Review
        fields = ('id', 'url', 'description', 'note', 'author', 'author_username',
                  'restaurant', 'restaurant_detail')

        
# MENU

class MenuSerializer(serializers.ModelSerializer):
    restaurant_url = serializers.HyperlinkedRelatedField(view_name='restaurant-detail',
                                                         read_only=True, source='restaurant')
    class Meta:
        model = Menu
        fields = ('id', 'url', 'name', 'price', 'description', 'restaurant_url')
        
class DishInMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ('id', 'url', 'name', 'ingredients', 'price', 'picture')

class NumberDishMenuSerializer(serializers.ModelSerializer):
    dish = DishInMenuSerializer()
    class Meta:
        model = NumberDishMenu
        fields = ('number', 'dish')        

class CategoryInMenuSerializer(serializers.ModelSerializer):
    dishes = DishInCategorySerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ('id', 'url', 'name', 'dishes')
        
class NumberCategoryMenuSerializer(serializers.ModelSerializer):
    category = CategoryInMenuSerializer()
    class Meta:
        model = NumberCategoryMenu
        fields = ('number', 'category')
        
class MenuDetailSerializer(serializers.ModelSerializer):
    offers = OfferSerializer(many=True, read_only=True)
    restaurant_detail = RestaurantInSerializer(read_only=True, source='restaurant')
    dishes = NumberDishMenuSerializer(many=True, source='numberdishmenu_set') 
    categories = NumberCategoryMenuSerializer(many=True, source='numbercategorymenu_set') 
    class Meta:
        model = Menu
        fields = ('id', 'name', 'price', 'description', 'dishes', 'categories', 'offers',
                  'restaurant', 'restaurant_detail')

# SCHEDULE

class ScheduleTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduleTime
        fields = ('opening_time', 'closing_time')
        
class ScheduleSerializer(serializers.ModelSerializer):
    restaurant_url = serializers.HyperlinkedRelatedField(view_name='restaurant-detail',
                                                         read_only=True, source='restaurant')
    times = ScheduleTimeSerializer(many=True, read_only=True)
    class Meta:
        model = Schedule
        fields = ('id', 'url', 'day', 'times', 'restaurant_url')  
        
class ScheduleDetailSerializer(serializers.ModelSerializer):
    restaurant_detail = RestaurantInSerializer(read_only=True, source='restaurant')
    times = ScheduleTimeSerializer(many=True)
    class Meta:
        model = Schedule
        fields = ('id', 'day', 'times', 'restaurant', 'restaurant_detail')  
