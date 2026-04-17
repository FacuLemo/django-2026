from django.http import HttpResponse
from django.shortcuts import render

from todolist.models import Tarea


def saludo(request):
    tareas = Tarea.objects.filter()
    return render(request,'saludo/index.html', {"tareas":tareas} )


def despedir(request):
    return render(request, 'saludo/despedir.html')



