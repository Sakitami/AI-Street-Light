from rest_framework import serializers
from models import Light


class LightSerializer(serializers.ModelSerializer):
    model = Light

    fields = ('light_id', 'air_index', 'pm25_index', 'status', 'group', 'rgb')
    # def create(self, validated_data):
    #     return Light.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.air_index = validated_data.get('air_index', instance.air_index)
    #     instance.pm25_index = validated_data.get('pm25_index', instance.pm25_index)
    #     instance.status = validated_data.get('status', instance.status)
    #     instance.group = validated_data.get('group', instance.group)
    #     instance.rgb = validated_data.get('rgb', instance.rgb)
    #     instance.save()
    #     return instance
