from django.contrib import admin

from .models import Dish, Restaurant

class DishAdmin(admin.ModelAdmin):
    list_display = ('name', 'ingredients_list', 'duration', 'price', 'restaurant')
    list_filter = ('ingredients',)
    search_fields = ('name', 'restaurant__name')
    def get_queryset(self, request):
        return super(DishAdmin, self).get_queryset(request).prefetch_related('ingredients')
    def ingredients_list(self, obj):
        return u", ".join(o.name for o in obj.ingredients.all())

class RestaurantAdmin(admin.ModelAdmin):
    fields = ('name', 'address')
    list_display = ('name', 'address', 'lat', 'lon')
    search_fields = ('name', 'address')

admin.site.register(Dish, DishAdmin)
admin.site.register(Restaurant, RestaurantAdmin)
