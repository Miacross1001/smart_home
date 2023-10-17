from django.urls import path
from .views import SensorListCreateView, SensorRetrieveUpdateView, TemperatureMeasurementListCreateView, SensorTemperatureMeasurementListCreateView


urlpatterns = [
    path('sensors/', SensorListCreateView.as_view()),
    path('sensors/<pk>/', SensorRetrieveUpdateView.as_view()),
    path('measurements/', TemperatureMeasurementListCreateView.as_view()),
    path('sensors/<sensor_pk>/measurements/', SensorTemperatureMeasurementListCreateView.as_view()),
]