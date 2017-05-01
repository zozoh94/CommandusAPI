from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from taggit.managers import TaggableManager
import moneyed
from djmoney.models.fields import MoneyField
from geopy.geocoders import Nominatim
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, null=True)
    lat = models.DecimalField(max_digits=10, decimal_places=8, null=True, blank=True, verbose_name='latitude')
    lon = models.DecimalField(max_digits=10, decimal_places=8, null=True, blank=True, verbose_name='longitude')
    picture = models.ImageField(upload_to='restaurant_picture', null=True, blank=True)
    def __str__(self):
        return self.name
    def pre_save(self):
        geolocator = Nominatim()
        location = geolocator.geocode(self.address)
        self.lat, self.lon = location.latitude, location.longitude

class Category(models.Model):
    name = models.CharField(max_length=255)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='categories', null=False)
    class Meta:
        verbose_name_plural = "categories"
    def __str__(self):
        return self.name
    
class Dish(models.Model):
    name = models.CharField(max_length=255)
    ingredients = TaggableManager(blank=True, verbose_name="Ingredients")
    duration = models.DurationField()
    price = MoneyField(max_digits=10, decimal_places=2, default_currency='EUR')
    picture = models.ImageField(upload_to='dish_picture', null=True, blank=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='dishes', null=False)
    categories = models.ManyToManyField(Category, related_name="dishes")
    class Meta:
        verbose_name_plural = "dishes"
    def menus(self):
        menus = []
        menus_a = self.menus.all()
        if(len(menus_a)):
            menus.extend(menus_a)
        for category in self.categories.all():
            menus_a = category.menus.all()
            if(len(menus_a)):
                menus.extend(menus_a)
        return menus
    def offers(self):
        offers = []
        offers_a = self.entry_offers.all()
        if(len(offers_a)):
            offers.extend(offers_a)
        for category in self.categories.all():
            offers_a = category.entry_offers.all()
            if(len(offers_a)):
                offers.extend(offers_a)
        return offers
    def __str__(self):
        return self.name

class Menu(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='menus', null=False)
    price = MoneyField(max_digits=10, decimal_places=2, default_currency='EUR')
    categories = models.ManyToManyField(
        Category,
        related_name='menus',
        through='NumberCategoryMenu',
        through_fields=('menu', 'category'),
    )
    dishes = models.ManyToManyField(
        Dish,
        related_name='menus',
        through='NumberDishMenu',
        through_fields=('menu', 'dish'),
    )
    def offers(self):
        return self.entry_offers.all()
    def __str__(self):
        return self.name

class NumberCategoryMenu(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    number = models.IntegerField()

class NumberDishMenu(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    number = models.IntegerField()
    
class Review(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='reviews', null=False)
    description = models.TextField(null=True, blank=True)
    note = models.IntegerField(default=5,
                               validators=[
                                   MaxValueValidator(10),
                                   MinValueValidator(0)
                               ]
    )
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
