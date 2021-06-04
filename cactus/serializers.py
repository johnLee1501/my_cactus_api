from django.contrib.auth.models import User
from rest_framework import serializers

from cactus.models import CactusModel


class CactusSerializer(serializers.ModelSerializer):
    class Meta:
        model = CactusModel
        fields = '__all__'
        extra_kwargs = {
            'cactus_id': {'read_only': True},
        }


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', "first_name", "last_name", "password")
        extra_kwargs = {
            'password': {'write_only': True},
        }