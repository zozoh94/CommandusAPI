from rest_framework import serializers

from .models import (Offer, Category, Dish, Menu,
                     NumberCategoryOfferEntry, NumberDishOfferEntry, NumberMenuOfferEntry,
                     NumberCategoryOfferDiscount, NumberDishOfferDiscount, NumberMenuOfferDiscount)
                     
from core.serializers import RestaurantSerializer

class OfferSerializer(serializers.ModelSerializer):
    restaurant_url = serializers.HyperlinkedRelatedField(view_name='restaurant-detail',
                                                         read_only=True, source='restaurant')
    class Meta:
        model = Offer
        fields = ('id', 'url', 'name', 'description', 'restaurant_url')

class CategoryInOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'url', 'name')

class DishInOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ('id', 'url', 'name')

class MenuInOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ('id', 'url', 'name')
        
class NumberCategoryOfferEntrySerializer(serializers.ModelSerializer):
    category = CategoryInOfferSerializer() 
    class Meta:
        model = NumberCategoryOfferEntry
        fields = ('number', 'category')

class NumberDishOfferEntrySerializer(serializers.ModelSerializer):
    dish = DishInOfferSerializer() 
    class Meta:
        model = NumberCategoryOfferEntry
        fields = ('number', 'dish')

class NumberMenuOfferEntrySerializer(serializers.ModelSerializer):
    dish = MenuInOfferSerializer() 
    class Meta:
        model = NumberCategoryOfferEntry
        fields = ('number', 'menu')

class NumberCategoryOfferDiscountSerializer(serializers.ModelSerializer):
    category = CategoryInOfferSerializer() 
    class Meta:
        model = NumberCategoryOfferDiscount
        fields = ('number', 'category')

class NumberDishOfferDiscountSerializer(serializers.ModelSerializer):
    dish = DishInOfferSerializer()
    class Meta:
        model = NumberDishOfferDiscount
        fields = ('number', 'dish')

class NumberMenuOfferDiscountSerializer(serializers.ModelSerializer):
    dish = MenuInOfferSerializer() 
    class Meta:
        model = NumberMenuOfferDiscount
        fields = ('number', 'menu')
        
class OfferDetailSerializer(serializers.ModelSerializer):
    restaurant_detail = RestaurantSerializer(read_only=True, source='restaurant')
    entry_categories = NumberCategoryOfferEntrySerializer(many=True, source='numbercategoryofferentry_set')
    entry_dishes = NumberDishOfferEntrySerializer(many=True, source='numberdishofferentry_set')
    entry_menus = NumberMenuOfferEntrySerializer(many=True, source='numbermenuofferentry_set')
    discount_categories = NumberCategoryOfferDiscountSerializer(many=True, source='numbercategoryofferdiscount_set')
    discount_dishes = NumberDishOfferDiscountSerializer(many=True, source='numberdishofferdiscount_set')
    discount_menus = NumberMenuOfferDiscountSerializer(many=True, source='numbermenuofferdiscount_set')
    class Meta:
        model = Offer
        fields = ('id', 'name', 'description', 'nbr_entries', 'nbr_discount',
                  'entry_categories', 'entry_dishes', 'entry_menus',
                  'discount_categories', 'discount_dishes', 'discount_menus',
                  'discount', 'discount_on_total', 'restaurant', 'restaurant_detail')
