from django.contrib import admin

# Register your models here.
from weather.models import Weather, Summary


class SummaryAdmin(admin.ModelAdmin):
    list_display = ['avg_temperature', 'avg_humidity', 'start_date', 'end_date']
    list_filter = ['avg_temperature', 'avg_humidity', 'start_date', 'end_date']

    def delete_model(self, request, obj):
        data = Weather.objects.filter(created_at__lte=obj.end_date, created_at__gte=obj.start_date)
        data.delete()
        obj.delete()

    def delete_queryset(self, request, queryset):
        for instance in queryset:
            self.delete_model(request, instance)
        queryset.delete()


class WeatherAdmin(admin.ModelAdmin):
    list_display = ['temperature', 'humidity', 'created_at']
    list_filter = ['temperature', 'humidity', 'created_at']


admin.site.register(Weather, WeatherAdmin)
admin.site.register(Summary, SummaryAdmin)
