from django.urls import path

from .views import ListCreateSensorView

urlpatterns = [
    path('sensors/', ListCreateSensorView.as_view())
]
