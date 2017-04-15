from django.db import models
from django.contrib.auth.models import AbstractUser
from geopy.geocoders import Nominatim

class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatar', null=True, blank=True)
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )
    gender = models.CharField(max_length=1, null=True, blank=True, choices=GENDER_CHOICES)
    
class Address(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='addresses', null=False)
    address = models.CharField(max_length=255, null=True)
    lat = models.DecimalField(max_digits=10, decimal_places=8, null=True, blank=True, verbose_name='latitude')
    lon = models.DecimalField(max_digits=10, decimal_places=8, null=True, blank=True, verbose_name='longitude')
    class Meta:
        verbose_name_plural = "addresses"
    def pre_save(self):
        geolocator = Nominatim()
        location = geolocator.geocode(self.address)
        self.lat, self.lon = location.latitude, location.longitude
    def __str__(self):
        return self.name
