from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from taggit.managers import TaggableManager
import moneyed
from djmoney.models.fields import MoneyField
from geopy.geocoders import Nominatim
from django.core.cache import cache
import json
from django.conf import settings
from urllib.request import urlopen
import logging

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, null=True)
    lat = models.DecimalField(max_digits=10, decimal_places=8, null=True, blank=True)
    lon = models.DecimalField(max_digits=10, decimal_places=8, null=True, blank=True)
    def __str__(self):
        return self.name
@receiver(pre_save, sender=Restaurant)
def pre_save(sender, instance, *args, **kwargs):
    geolocator = Nominatim()
    location = geolocator.geocode(instance.address)
    instance.lat, instance.lon = location.latitude, location.longitude

class Dish(models.Model):
    name = models.CharField(max_length=255)
    ingredients = TaggableManager(blank=True, verbose_name="Ingredients")
    duration = models.DurationField()
    price = MoneyField(max_digits=10, decimal_places=2, default_currency='EUR')
    picture = models.ImageField(upload_to='dish_picture', null=True, blank=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='dishes', null=False)
    def ingredients_with_pictures(self):
        ingredients = []
        for ingredient in self.ingredients.names():
            if cache.get(ingredient) is not None:
                ingredients.append({'name': ingredient, 'picture': cache.get(ingredient)})                
            else:
                logger = logging.getLogger(__name__)
                picture = None
                serialized_data = urlopen(settings.PIXABAY_API_URL+'?key='+settings.PIXABAY_API_KEY
                                          +'&q='+ingredient+'&per_page=3&safesearch=true&lang=fr').read()
                logger.error(settings.PIXABAY_API_URL+'?key='+settings.PIXABAY_API_KEY
                                          +'&q='+ingredient+'&per_page=3&safesearch=true&lang=fr')
                data = json.loads(serialized_data)                
                logger.error(data)
                if data['hits']:
                    picture = data['hits'][0]['webformatURL']
                    cache.set(ingredient, picture, None)
                else:
                    cache.set(ingredient, picture, 1296000) 
                ingredients.append({'name': ingredient, 'picture': picture})
        return ingredients
    def __str__(self):
        return self.name
