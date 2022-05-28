from django.shortcuts import get_object_or_404
from rest_framework import serializers
from phonenumber_field.modelfields import PhoneNumberField

from .models import CustomUser


class UserSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=15)
    password = serializers.CharField()

    def validate(self, attrs):
        phone_number = attrs.get('phone_number')
        user = get_object_or_404(CustomUser, phone_number=phone_number)
        attrs["user"] = user
        return super().validate(attrs)

