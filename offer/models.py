from django.db import models

from core.models import Category, Dish, Menu, Restaurant

class Offer(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='offers', null=False)
    nbr_entries = models.IntegerField(verbose_name='minimum entries number') 
    nbr_discount = models.IntegerField(verbose_name='maximum discount number')
    entry_categories = models.ManyToManyField(
        Category,
        related_name='entry_offers',
        through='NumberCategoryOfferEntry',
        through_fields=('offer', 'category'),
    )
    entry_dishes = models.ManyToManyField(
        Dish,
        related_name='entry_offers',
        through='NumberDishOfferEntry',
        through_fields=('offer', 'dish'),
    )
    entry_menus = models.ManyToManyField(
        Menu,
        related_name='entry_offers',
        through='NumberMenuOfferEntry',
        through_fields=('offer', 'menu'),
    )
    discount_categories = models.ManyToManyField(
        Category,        
        related_name='discount_offers',
        through='NumberCategoryOfferDiscount',
        through_fields=('offer', 'category'),
    )
    discount_dishes = models.ManyToManyField(
        Dish,
        related_name='discount_offers',
        through='NumberDishOfferDiscount',
        through_fields=('offer', 'dish'),
    )
    discount_menus = models.ManyToManyField(
        Menu,
        related_name='discount_offers',
        through='NumberMenuOfferDiscount',
        through_fields=('offer', 'menu'),
    )
    discount = models.IntegerField(verbose_name='discount on the offer')
    discount_on_total = models.IntegerField(verbose_name='discount on the total')
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
