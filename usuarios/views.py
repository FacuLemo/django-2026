from django.shortcuts import render, redirect

from .forms import UsuarioPersonalizadoForm
from django.contrib.auth import login

# Create your views here.

def registrarse(request):
    if request.method == 'POST':
        form = UsuarioPersonalizadoForm(request.POST, request.FILES)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect('tareas')
    else:
        form = UsuarioPersonalizadoForm()
    return render(request, 'registration/register.html', {"form":form})