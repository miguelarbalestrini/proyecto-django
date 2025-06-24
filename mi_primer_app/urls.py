from django.urls import path

from .views import saludo

urlpatterns = [
    path('hola-mundo/', saludo),
]
