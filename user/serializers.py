from rest_framework import serializers
from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)
from django.contrib.auth import get_user_model
from .models import Address

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('name', 'address')

class MyUserDetailsSerializer(TaggitSerializer, serializers.ModelSerializer):
    addresses = AddressSerializer(many=True)
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name', 'gender', 'avatar', 'addresses')
        read_only_fields = ('email',)
