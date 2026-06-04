from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required, permission_required
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


from .forms import TareaForm
from .models import Tarea


@login_required
@permission_required('todolist.view_tarea') #nombre_app.accion_modelo (minuscula)
def tareas(request):
    tareas = Tarea.objects.filter(activo=True)
    return render(request, "todolist/index.html", {"tareas": tareas})

@login_required
@permission_required('todolist.add_tarea') #nombre_app.accion_modelo
def crear_tarea(request):
    if request.method == "POST":
        form = TareaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("tareas")
    else:
        form = TareaForm()
    return render(request, "todolist/crear_tarea.html", {"form": form})

# Parametro Ruta: url.com/tarea/5
# Query Param: url.com/tarea?clave=valor&clave_dos=valor&clave_tres=valor

@login_required
@permission_required('todolist.change_tarea') #nombre_app.accion_modelo
def editar_tarea(request, id):
    tarea = get_object_or_404(Tarea, id=id)

    if request.method == "POST":
        form = TareaForm(request.POST,request.FILES, instance=tarea)
        if form.is_valid():
            form.save()
            #logica extra
            return redirect("tareas")
    else:
        form = TareaForm(instance=tarea)

    return render(request, "todolist/editar_tarea.html", {"form": form})

@login_required
@permission_required('todolist.delete_tarea')
def eliminar_tarea(request, id):

    tarea = get_object_or_404(Tarea, id=id)

    if request.method == "POST":
        # tarea.delete() <--- BORRADO LITERAL, se elimina el registro de la db.
        tarea.activo = False
        tarea.save()

        return redirect("tareas")

    return render(request, "todolist/borrar_tarea.html", {"tarea": tarea})

#----- VISTAS BASADAS EN CLASES (cvb):

class GetTareas(LoginRequiredMixin, ListView): # GET ALL TAREAS
    model = Tarea
    template_name = "todolist/index.html"
    context_object_name = 'tareas' #nombre de los datos en el template

#GET TAREA BY ID: DetailView

class CreateTareas(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model=Tarea
    form_class= TareaForm
    template_name="todolist/crear_tarea.html"
    success_url = reverse_lazy("tareas")
    permission_required = "todolist.add_tarea"

class UpdateTareas(LoginRequiredMixin, UpdateView):
    model= Tarea
    template_name= "todolist/editar_tarea.html"
    form_class = TareaForm
    success_url = reverse_lazy("tareas")

class DeleteTareas(LoginRequiredMixin, DeleteView):
    model=Tarea
    template_name = "todolist/borrar_tarea.html"
    success_url= reverse_lazy("tareas")








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
