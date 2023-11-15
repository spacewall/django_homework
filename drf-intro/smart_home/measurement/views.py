from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from .models import Sensor, Measurement
from .serializers import SensorDetailSerializer, MeasurmentSerializer


class ListCreateSensorView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer
