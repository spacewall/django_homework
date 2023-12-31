from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=100, blank=True)

    def __str__(self) -> str:
        return f'{str(self.name)} ({str(self.id)})'


class Measurement(models.Model):
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    sensor = models.ForeignKey(Sensor, related_name='measurements', on_delete=models.CASCADE, related_query_name='sensor')

    def __str__(self) -> str:
        return f'{str(self.sensor.name)} ({str(self.sensor.id)})'
