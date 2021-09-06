from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Avg, F


# Create your models here.
class Weather(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    temperature = models.FloatField(validators=[MinValueValidator(19), MaxValueValidator(28)])
    humidity = models.FloatField(validators=[MinValueValidator(35), MaxValueValidator(65)])

    class Meta:
        ordering = ['-id']


class Summary(models.Model):
    avg_temperature = models.FloatField()
    avg_humidity = models.FloatField()
    start_date = models.DateTimeField(null=True,blank=True)
    end_date = models.DateTimeField(null=True,blank=True)


@receiver(signal=post_save, sender='weather.Weather')
def checkout_post_save(sender, instance, created, **kwargs):
    if created:
        if Weather.objects.count() % 10 == 0:
            latest_weather_data = Weather.objects.all()[:10]
            summary_data = latest_weather_data.aggregate(avg_temp=Avg(F('temperature')),
                                                         avg_humidity=Avg(F('humidity')))

            Summary.objects.create(avg_temperature=summary_data['avg_temp'],
                                   avg_humidity=summary_data['avg_humidity'],
                                   start_date=latest_weather_data[9].created_at,
                                   end_date=instance.created_at)
