
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("saludo.urls")),
    path("tareas/", include("todolist.urls")),
]
