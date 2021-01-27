from rest_framework import serializers

from cactus.models import CactusModel


class CactusSerializer(serializers.ModelSerializer):
    class Meta:
        model = CactusModel
        fields = '__all__'
        extra_kwargs = {
            'cactus_id': {'read_only': True},
        }
