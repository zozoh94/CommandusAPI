from django.contrib import admin

from .models import Dish, Restaurant, Category, Menu, NumberCategoryMenu

class DishAdmin(admin.ModelAdmin):
    list_display = ('name', 'ingredients_list', 'duration', 'price', 'restaurant', 'categories_list')
    list_display_links = ('name', 'restaurant')
    list_filter = ('ingredients', 'categories')
    search_fields = ('name', 'restaurant__name', 'ingredients__name', 'categories__name')
    filter_horizontal = ('categories',)
    def get_queryset(self, request):
        return super(DishAdmin, self).get_queryset(request).prefetch_related('ingredients')
    def ingredients_list(self, obj):
        return u", ".join(o.name for o in obj.ingredients.all())
    def categories_list(self, obj):
        return u", ".join(o.name for o in obj.categories.all())

class RestaurantAdmin(admin.ModelAdmin):
    fields = ('name', 'address', 'picture')
    list_display = ('name', 'address', 'lat', 'lon')
    search_fields = ('name', 'address')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'restaurant')
    list_display_links = ('name', 'restaurant')
    list_filter = ('restaurant',)
    search_fields = ('name', 'restaurant__name')

class NumberCategoryMenuInline(admin.StackedInline):
    model = NumberCategoryMenu
    extra = 1
    
class MenuAdmin(admin.ModelAdmin):
    fields = ('name', 'restaurant')
    inlines = (NumberCategoryMenuInline,)
    list_display = ('name', 'restaurant')
    list_display_links = ('name', 'restaurant',)
    list_filter = ('restaurant',)
    search_fields = ('name', 'restaurant__name')


admin.site.register(Dish, DishAdmin)
admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Menu, MenuAdmin)
