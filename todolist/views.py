from django.shortcuts import render, redirect

from .models import Tarea
from .forms import TareaForm



def tareas(request):
    tareas = Tarea.objects.all()
    return render(request, "todolist/index.html", {"tareas": tareas})


def crear_tarea(request):
    if request.method == "POST":
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tareas')
    else:
        form = TareaForm()
    
    return render(request, 'todolist/crear_tarea.html', {"form":form})
    






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
