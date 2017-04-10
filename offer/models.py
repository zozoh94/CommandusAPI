from django.db import models

from core.models import Category, Dish, Menu, Restaurant

class Offer(models.Model):
    name = models.CharField(max_length=255)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='offers', null=False)
    nbrEntries = models.IntegerField(verbose_name='minimum entries number') 
    nbrDiscount = models.IntegerField(verbose_name='maximum discount number')
    entryCategories = models.ManyToManyField(
        Category,
        related_name='entryOffers',
        through='NumberCategoryOfferEntry',
        through_fields=('offer', 'category'),
    )
    entryDishes = models.ManyToManyField(
        Dish,
        related_name='entryOffers',
        through='NumberDishOfferEntry',
        through_fields=('offer', 'dish'),
    )
    entryMenus = models.ManyToManyField(
        Menu,
        related_name='entryOffers',
        through='NumberMenuOfferEntry',
        through_fields=('offer', 'menu'),
    )
    discountCategories = models.ManyToManyField(
        Category,        
        related_name='discountOffers',
        through='NumberCategoryOfferDiscount',
        through_fields=('offer', 'category'),
    )
    discountDishes = models.ManyToManyField(
        Dish,
        related_name='discountOffers',
        through='NumberDishOfferDiscount',
        through_fields=('offer', 'dish'),
    )
    discountMenus = models.ManyToManyField(
        Menu,
        related_name='discountOffers',
        through='NumberMenuOfferDiscount',
        through_fields=('offer', 'menu'),
    )
    discount = models.IntegerField(verbose_name='discount on the offer')
    discountOnTotal = models.IntegerField(verbose_name='discount on the total')
    def __str__(self):
        return self.name

class NumberCategoryOfferEntry(models.Model):
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    number = models.IntegerField()
    class Meta:
        verbose_name_plural = "categories entries"    
    
class NumberDishOfferEntry(models.Model):
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    number = models.IntegerField()
    class Meta:
        verbose_name_plural = "dishes entries" 
    
class NumberMenuOfferEntry(models.Model):
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    number = models.IntegerField()
    class Meta:
        verbose_name_plural = "menus entries" 

class NumberCategoryOfferDiscount(models.Model):
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    number = models.IntegerField()
    class Meta:
        verbose_name_plural = "categories discounts" 
    
class NumberDishOfferDiscount(models.Model):
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    number = models.IntegerField()
    class Meta:
        verbose_name_plural = "dishes discounts"
    
class NumberMenuOfferDiscount(models.Model):
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    number = models.IntegerField()
    class Meta:
        verbose_name_plural = "menus discounts"
