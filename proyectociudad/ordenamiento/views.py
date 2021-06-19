from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext
# Importar modelos
from ordenamiento.models import *
# Importar formularios
from ordenamiento.forms import *


def index(request):

    """
    Listar los barrios y parroquias
    :param request:
    :return: parroauias y barrios
    """
    parroquia = Parroquia.objects.all()
    barrio = Barrio.objects.all()
    informacion_template = {'barrio':barrio, 'parroquia':parroquia}
    return render(request,'index.html',informacion_template)

"""
Barrio
"""

def crear_barrio(request):
    if request.method == 'POST':
        formulario = BarrioForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = BarrioForm()
    diccionario = {'formulario': formulario}

    return render(request,'crearBarrio.html',diccionario)

def editar_barrio(request, id):
    barrio = Barrio.objects.get(pk=id)
    if request.method == 'POST':
        formulario = BarrioForm(request.POST, instance=barrio)
        print(formulario.errors)
        if formulario.isvalid():
            formulario.save()
            return redirect(index)
    else:
        formulario = BarrioForm(instance=barrio)
    diccionario = {'formulario': formulario}
    return render(request, 'editarBarrio.html', diccionario)


"""
Parroquia
"""

def crear_parroquia(request):
    if request.method == 'POST':
        formulario = ParroquiaForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = ParroquiaForm()
    diccionario = {'formulario': formulario}

    return render(request,'crearParroquia.html',diccionario)

def editar_parroquia(request, id):
    parroquia = Parroquia.objects.get(pk=id)
    if request.method=='POST':
        formulario = ParroquiaForm(request.POST, instance=parroquia)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = ParroquiaForm(instance=parroquia)
    diccionario = {'formulario': formulario}
    return render(request, 'editarParroquia.html', diccionario)

"""
Listar Barrio
"""

def listar_barrio(request):

    barrio = Barrio.objects.all()
    informacion = {'barrio': barrio}
    return render(request, 'listarBarrios.html', informacion)