# Generated by Django 3.2.7 on 2021-09-06 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Summary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avg_temperature', models.FloatField()),
                ('avg_humidity', models.FloatField()),
                ('start_date', models.DateTimeField()),
                ('end_data', models.DateTimeField()),
            ],
        ),
    ]
