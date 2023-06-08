from rest_framework import serializers
from .models import Light


class LightSerializer(serializers.ModelSerializer):
    """Light Status"""

    class Meta:
        model = Light

        fields = ('light_id', 'air_index', 'pm25_index', 'status', 'group', 'rgb')


class LightStatusDown(serializers.ModelSerializer):
    """Light Download Status"""

    class Meta:
        model = Light

        fields = ('light_id', 'group', 'rgb')


class LightStatusUp(serializers.ModelSerializer):
    """Light Upload Status"""

    class Meta:
        model = Light

        fields = ('air_index', 'pm25_index', 'status', 'group', 'rgb')
