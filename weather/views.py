from django.shortcuts import render
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

# Create your views here.
from weather.models import Weather
from weather.serializers import WeatherSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import render


class WeatherViewSet(ModelViewSet):
    serializer_class = WeatherSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['temperature', 'humidity']
    queryset = Weather.objects.all()
    renderer_classes = (JSONRenderer, TemplateHTMLRenderer,)
    template_name = "weather_data_list.html"

    def list(self, request, *args, **kwargs):
        response = super(WeatherViewSet, self).list(request, *args, **kwargs)
        if request.accepted_renderer.format == 'html':
            return Response({'data': WeatherSerializer(self.get_queryset(), many=True).data},
                            template_name=self.template_name)
        return response

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({'data': WeatherSerializer(self.get_queryset(), many=True).data},
                        template_name=self.template_name)


from django.shortcuts import render

from django.shortcuts import render


def weather_detail_view(request):
    return render(request, "weather-detail.html")
