from django.contrib import admin

from .models import (Dish, Restaurant, Category, Menu,
                     NumberCategoryMenu, NumberDishMenu,
                     Review, Schedule, ScheduleTime)

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

class ReviewInline(admin.StackedInline):
    model = Review
    extra = 0
    
class RestaurantAdmin(admin.ModelAdmin):
    fields = ('name', 'address', 'picture')
    inlines = (ReviewInline,)
    list_display = ('name', 'address', 'lat', 'lon')
    search_fields = ('name', 'address')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'restaurant')
    list_display_links = ('name', 'restaurant')
    list_filter = ('restaurant',)
    search_fields = ('name', 'restaurant__name')

class NumberCategoryMenuInline(admin.StackedInline):
    model = NumberCategoryMenu
    extra = 0

class NumberDishMenuInline(admin.StackedInline):
    model = NumberDishMenu
    extra = 0
    
class MenuAdmin(admin.ModelAdmin):
    fields = ('name', 'description', 'restaurant', 'price')
    inlines = (NumberCategoryMenuInline, NumberDishMenuInline)
    list_display = ('name', 'restaurant')
    list_display_links = ('name', 'restaurant',)
    list_filter = ('restaurant',)
    search_fields = ('name', 'restaurant__name')

class ScheduleTimeInline(admin.TabularInline):
    model = ScheduleTime
    extra = 0
    
class ScheduleAdmin(admin.ModelAdmin):
    fields = ('day', 'restaurant')
    inlines = (ScheduleTimeInline,)
    list_filter = ('restaurant', 'day')
    search_fields = ('restaurant__name',)
    
admin.site.register(Dish, DishAdmin)
admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Menu, MenuAdmin)
admin.site.register(Schedule, ScheduleAdmin)
