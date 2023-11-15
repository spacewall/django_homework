from django.urls import path

from .views import ListCreateSensorView, RetrieveUpdateSensorView, CreateMeasurementView

urlpatterns = [
    path('sensors/', ListCreateSensorView.as_view()),
    path('sensors/<pk>/', RetrieveUpdateSensorView.as_view()),
    path('measurements/', CreateMeasurementView.as_view())
]
