from django.contrib import admin
from django import forms

from .models import (Offer,
                     NumberCategoryOfferEntry, NumberDishOfferEntry, NumberMenuOfferEntry,
                     NumberCategoryOfferDiscount, NumberDishOfferDiscount, NumberMenuOfferDiscount)

class NumberCategoryOfferEntryInline(admin.TabularInline):
    model = NumberCategoryOfferEntry
    extra = 1

class NumberDishOfferEntryInline(admin.TabularInline):
    model = NumberDishOfferEntry
    extra = 1

class NumberMenuOfferEntryInline(admin.TabularInline):
    model = NumberMenuOfferEntry
    extra = 1

class NumberCategoryOfferDiscountInline(admin.TabularInline):
    model = NumberCategoryOfferDiscount
    extra = 1

class NumberDishOfferDiscountInline(admin.TabularInline):
    model = NumberDishOfferDiscount
    extra = 1

class NumberMenuOfferDiscountInline(admin.TabularInline):
    model = NumberMenuOfferDiscount
    extra = 1
    
class OfferAdmin(admin.ModelAdmin):
    fields = ('name', 'description', 'restaurant', 'nbr_entries', 'nbr_discount', 'discount', 'discount_on_total')
    inlines = (NumberCategoryOfferEntryInline, NumberDishOfferEntryInline, NumberMenuOfferEntryInline,
               NumberCategoryOfferDiscountInline, NumberDishOfferDiscountInline, NumberMenuOfferDiscountInline)
    list_display = ('name', 'restaurant')
    list_display_links = ('name', 'restaurant',)
    list_filter = ('restaurant',)
    search_fields = ('name', 'restaurant__name')

admin.site.register(Offer, OfferAdmin)
