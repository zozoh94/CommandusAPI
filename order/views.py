from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework import status
from django.http import Http404
from django.core.exceptions import SuspiciousOperation
from core.models import Menu, Dish, Restaurant
import json

@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def calculate_basket_price(request):
    #Basket verification
    restaurant_id = request.data.get('restaurant')
    if restaurant_id is None:
        return Response({'detail' : 'Please specify a restaurant parameter.'},
                        status=status.HTTP_400_BAD_REQUEST)
    try:
        restaurant = Restaurant.objects.get(id=restaurant_id)
    except Restaurant.DoesNotExist:
        raise Http404("Restaurant does not exist")
    
    dishes_ids = request.data.get('dishes')
    menus_o = request.data.get('menus')

    dishes = []
    if dishes_ids:
        for dish_id in dishes_ids:
            try:
                dish = Dish.objects.get(id=dish_id)
            except Dish.DoesNotExist:
                raise Http404("Dish does not exist")
            if dish.restaurant != restaurant:
                raise SuspiciousOperation("Dish restaurant error")
            dishes.append(dish)

    menus = []
    if menus_o:
        for menu_o in menus_o:
            try:
                menu = Menu.objects.get(id=menu_o.get('id'))
            except Menu.DoesNotExist:
                raise Http404("Menu does not exist")
            if menu.restaurant != restaurant:
                raise SuspiciousOperation("Menu restaurant error")
            if menu_o.get('dishes'):
                for dish_id in menu_o.get('dishes'):
                    try:
                        dish = Dish.objects.get(id=dish_id)
                    except Dish.DoesNotExist:
                        raise Http404("Dish in menu does not exist")
                    if dish.restaurant != restaurant:
                        raise SuspiciousOperation("Dish in menu restaurant error")

                    if dish not in menu.dishes.all():
                        for category in dish.categories.all():
                            if category not in menu.categories.all():
                                raise SuspiciousOperation("Dish not in menu dishes or categories")
            else:
                raise SuspiciousOperation("No dishes in menu")
                                
            menus.append(menu)

    price = 0
    for menu in menus:
        price += menu.price.amount
    for dish in dishes:
        price += dish.price.amount     
        
    return Response({"offers": [], "price": price})
