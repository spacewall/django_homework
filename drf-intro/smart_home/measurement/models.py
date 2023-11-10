from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=100, blank=True)


class Measurement(models.Model):
    id = models.BigIntegerField(primary_key=True)
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True, auto_now=True)
