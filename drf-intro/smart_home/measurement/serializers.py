from rest_framework import serializers

from models import Measurement, Sensor

# TODO: опишите необходимые сериализаторы
class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['name', 'description']


class MeasurmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['id', 'temperature', 'created_at']
