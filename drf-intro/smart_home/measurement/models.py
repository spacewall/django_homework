from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=100, blank=True)


class Measurement(models.Model):
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now=True)

    sensor = models.ForeignKey(Sensor, related_name='measurements', on_delete=models.CASCADE)
