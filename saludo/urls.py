# saludos/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path("", views.saludo, name="saludo"),
    path("despedir/", views.despedir, name="adios"),
]
