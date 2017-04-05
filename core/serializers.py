from rest_framework import serializers
from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)

from .models import Dish

class DishSerializer(TaggitSerializer, serializers.ModelSerializer):
    ingredients = TagListSerializerField(required=False)
    class Meta:
        model = Dish
        fields = ('id', 'name', 'ingredients', 'price', 'picture')

class DishDetailSerializer(DishSerializer):
    class Meta:
        model = Dish
        fields = ('id', 'name', 'ingredients_with_pictures', 'duration', 'price', 'picture')
