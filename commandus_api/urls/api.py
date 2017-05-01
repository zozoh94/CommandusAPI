from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers

from core import views as core_views
from user import views as user_views
from offer import views as offer_views

router = routers.DefaultRouter()
router.register(r'dish', core_views.DishViewSet)
router.register(r'restaurant', core_views.RestaurantViewSet)
router.register(r'menu', core_views.MenuViewSet)
router.register(r'category', core_views.CategoryViewSet)
router.register(r'review', core_views.ReviewViewSet)
router.register(r'offer', offer_views.OfferViewSet)

urlpatterns = [    
    url(r'^', include(router.urls)),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^auth/registration/verify-email/login/$', user_views.VerifyEmailLoginAutoView.as_view(), name='rest_verify_email_login_auto'),
    url(r'^auth/facebook/$', user_views.FacebookLogin.as_view(), name='fb_login'),
    url(r'^auth/google/$', user_views.GoogleLogin.as_view(), name='google_login'),
    url(r'^auth/twitter/$', user_views.TwitterLogin.as_view(), name='twitter_login'),
    url(r'^auth/', include('rest_auth.urls')),
    url(r'^auth/registration/', include('rest_auth.registration.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^robots.txt$', lambda r: HttpResponse("User-agent: *\nDisallow: /", content_type="text/plain"))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
