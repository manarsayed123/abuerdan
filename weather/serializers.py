from rest_framework import serializers

from weather.models import Weather


class WeatherSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)
    class Meta:
        model = Weather
        fields = '__all__'

