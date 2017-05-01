from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from taggit.managers import TaggableManager
import moneyed
from djmoney.models.fields import MoneyField
from geopy.geocoders import Nominatim
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings
from datetime import time, date, datetime, timedelta
    
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
    def location(self):
        return {'lat': self.lat, 'lon': self.lon }
    def open(self):
        date_now = date.today()
        now = datetime.today()
        day = now.weekday()
        for schedule in self.schedules.all():
            if schedule.day == day:
                for time in schedule.times.all():
                    opening = datetime.combine(date_now, time.opening_time)
                    if time.opening_time < time.closing_time:
                        closing = datetime.combine(date_now, time.closing_time)
                    else:
                        closing = datetime.combine(date_now + timedelta(1), time.closing_time)
                    if opening < now and now < closing:
                        return True
        return False
            

class Schedule(models.Model):    
    DAY_CHOICES = ((0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'), (3, 'Thursday'),
                       (4, 'Friday'), (5, 'Saturday'), (6, 'Sunday'))
    day = models.SmallIntegerField(null=False, choices=DAY_CHOICES)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='schedules', null=False)
    ordering = ('day',)
    def __str__(self):
        string = str(dict(self.DAY_CHOICES).get(self.day)) + ' ('
        for i, time in enumerate(self.times.all()):
            string += time.opening_time.strftime('%H:%M') + '-' + time.closing_time.strftime('%H:%M')
            if i < len(self.times.all())-1:
                string += ', '
        return string + ')'
        
class ScheduleTime(models.Model):
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE, related_name='times', null=False)
    
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
