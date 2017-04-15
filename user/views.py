from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.twitter.views import TwitterOAuthAdapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from allauth.socialaccount.providers.oauth.client import OAuthClient
from rest_auth.registration.views import SocialLoginView, VerifyEmailView
from django.contrib.auth import get_user_model
from django.conf import settings
from rest_auth.app_settings import TokenSerializer
from rest_framework.authtoken.models import Token

class VerifyEmailLoginAutoView(VerifyEmailView):
    response_serializer = TokenSerializer
    token_model = Token
    def post(self, request, *args, **kwargs):
        self.kwargs['key'] = self.request.data.get('key', '')
        confirmation = self.get_object()
        confirmation.confirm(self.request)
        self.user = get_user_model().objects.get(email=confirmation.email_address.email)
        self.user.backend = 'django.contrib.auth.backends.ModelBackend'
        self.token, created = self.token_model.objects.get_or_create(
            user=self.user)
        if getattr(settings, 'REST_SESSION_LOGIN', True):
            login(self.request, self.user)
        return Response(
            self.response_serializer(self.token).data, status=status.HTTP_200_OK
        )

class SocialLoginMixin(object):
    def initialize_request(self, request, *args, **kwargs):
        request =  super(SocialLoginMixin, self).initialize_request(request, *args, **kwargs)
        self.callback_url = request.data['redirectUri']
        return request

class FacebookLogin(SocialLoginMixin, SocialLoginView):
    adapter_class = FacebookOAuth2Adapter
    client_class = OAuth2Client   
class GoogleLogin(SocialLoginMixin, SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    client_class = OAuth2Client   
class TwitterLogin(SocialLoginMixin, SocialLoginView):
    adapter_class = TwitterOAuthAdapter
    client_class = OAuthClient
