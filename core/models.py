from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from taggit.managers import TaggableManager
import moneyed
from djmoney.models.fields import MoneyField
from geopy.geocoders import Nominatim

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
    def __str__(self):
        return self.name
    def clean(self):
        for category in self.categories.all():
            if category.restaurant != self.restaurant:
                raise ValidationError({'categories': _('There is one or many categories which are not associated to '
                                                       + 'the restaurant of the dish.')})
class Menu(models.Model):
    name = models.CharField(max_length=255)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='menus', null=False)
    categories = models.ManyToManyField(
        Category,
        through='NumberCategoryMenu',
        through_fields=('menu', 'category'),
    )
    def __str__(self):
        return self.name

class NumberCategoryMenu(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    number = models.IntegerField()
