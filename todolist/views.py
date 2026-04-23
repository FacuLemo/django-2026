from django.shortcuts import get_object_or_404, redirect, render

from .forms import TareaForm
from .models import Tarea


def tareas(request):
    tareas = Tarea.objects.filter(activo=True).order_by("-id")
    return render(request, "todolist/index.html", {"tareas": tareas})


def crear_tarea(request):
    if request.method == "POST":
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("tareas")
    else:
        form = TareaForm()

    return render(request, "todolist/crear_tarea.html", {"form": form})


# Parametro Ruta: url.com/tarea/5
# Query Param: url.com/tarea?clave=valor&clave_dos=valor&clave_tres=valor


def editar_tarea(request, id):

    tarea = get_object_or_404(Tarea, id=id)

    if request.method == "POST":
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect("tareas")
    else:
        form = TareaForm(instance=tarea)

    return render(request, "todolist/editar_tarea.html", {"form": form})


def eliminar_tarea(request, id):

    tarea = get_object_or_404(Tarea, id=id)

    if request.method == "POST":
        # tarea.delete() <--- BORRADO LITERAL, se elimina el registro de la db.
        tarea.activo = False
        tarea.save()

        return redirect("tareas")

    return render(request, "todolist/borrar_tarea.html", {"tarea": tarea})


"""

    # LOOKUPS - obtención de datos desde el orm


    #get by id
    tareas = Tarea.objects.get(id=2)

    #str
    tareas = Tarea.objects.filter(nombre__icontains="bugfix")


    #int y floats
    posteos = Posteos.objects.filter(likes__gt=10)
    posteos = Posteos.objects.filter(likes__gte=10)
    posteos = Posteos.objects.filter(likes__lt=100)
    posteos = Posteos.objects.filter(likes__lte=100)
    posteos = Posteos.objects.filter(likes__range=(10,100))

    #listas
    tareas = Tarea.objects.filter(etiquetas__in=["Urgente",2025])

    #fecha
    tareas = Tarea.objects.filter(fecha_completado__year=2025)
    tareas.filter(fecha_completado__month=3)

    #saber si en nulo
    tareas = Tarea.objects.filter(responsable__isnull=False)

    tareas = Tarea.objects.filter(responsable__username="Facundo")
"""
