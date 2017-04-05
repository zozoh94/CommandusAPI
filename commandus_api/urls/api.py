from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers

from core import views as core_views

router = routers.DefaultRouter()
router.register(r'dish', core_views.DishViewSet)
router.register(r'restaurant', core_views.RestaurantViewSet)

urlpatterns = [    
    url(r'^', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
