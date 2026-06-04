#URLS DE TODOLIST
from django.urls import path
from . import views

urlpatterns = [
    path("", views.tareas, name="tareas"),
    path("nueva/", views.crear_tarea, name="crear_tarea"),
    path("editar/<int:id>/", views.editar_tarea, name="editar"),
    path("borrar/<int:id>/", views.eliminar_tarea, name="borrar"),
    #--------- class based views:
    path("cbv/", views.GetTareas.as_view()),
    path("cbv/nueva/", views.CreateTareas.as_view()),
    path("cbv/editar/<int:pk>/", views.UpdateTareas.as_view()),
    path("cbv/borrar/<int:pk>/", views.DeleteTareas.as_view()),


]
