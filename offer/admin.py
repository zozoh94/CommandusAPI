from django.contrib import admin
from django import forms

from .models import (Offer,
                     NumberCategoryOfferEntry, NumberDishOfferEntry, NumberMenuOfferEntry,
                     NumberCategoryOfferDiscount, NumberDishOfferDiscount, NumberMenuOfferDiscount)

class NumberCategoryOfferEntryInline(admin.TabularInline):
    model = NumberCategoryOfferEntry
    extra = 0

class NumberDishOfferEntryInline(admin.TabularInline):
    model = NumberDishOfferEntry
    extra = 0

class NumberMenuOfferEntryInline(admin.TabularInline):
    model = NumberMenuOfferEntry
    extra = 0

class NumberCategoryOfferDiscountInline(admin.TabularInline):
    model = NumberCategoryOfferDiscount
    extra = 0

class NumberDishOfferDiscountInline(admin.TabularInline):
    model = NumberDishOfferDiscount
    extra = 0

class NumberMenuOfferDiscountInline(admin.TabularInline):
    model = NumberMenuOfferDiscount
    extra = 0
    
class OfferAdmin(admin.ModelAdmin):
    fields = ('name', 'description', 'restaurant', 'nbr_entries', 'nbr_discount', 'discount', 'discount_on_total')
    inlines = (NumberCategoryOfferEntryInline, NumberDishOfferEntryInline, NumberMenuOfferEntryInline,
               NumberCategoryOfferDiscountInline, NumberDishOfferDiscountInline, NumberMenuOfferDiscountInline)
    list_display = ('name', 'restaurant')
    list_display_links = ('name', 'restaurant',)
    list_filter = ('restaurant',)
    search_fields = ('name', 'restaurant__name')

admin.site.register(Offer, OfferAdmin)
