from django.urls import path, include
from rest_framework.routers import DefaultRouter

from weather.views import WeatherViewSet, weather_detail_view

router = DefaultRouter()
router.register('weather', WeatherViewSet, basename='weather_crud')

urlpatterns = [
    path('', include(router.urls)),
    path('add-weather/', weather_detail_view, name="weather_detail_view"),

]
