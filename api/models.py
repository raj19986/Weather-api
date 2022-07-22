from django.db import models

# Create your models here.

class WeatherData(models.Model):
    city=models.CharField(max_length=100)
    data=models.JSONField(null=True)
