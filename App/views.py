from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from App.forms import *

def inicio(request):
    return render(request, "App/inicio.html")

def padres(request):

    if request.method == 'POST':
        formulario=PadreForm(request.POST)
        if formulario.is_valid():
            informacion=formulario.cleaned_data
            padre=Padre(nombre=informacion['nombre'], edad=informacion['edad'])
            padre.save()
            return render(request, "App/inicio.html")
    else:
        formulario=PadreForm()
    return render(request, "App/padres.html", {'formulario':formulario})


def madres(request):
    
    if request.method == 'POST':
        formulario=MadreForm(request.POST)
        if formulario.is_valid():
            informacion=formulario.cleaned_data
            madre=Madre(nombre=informacion['nombre'], edad=informacion['edad'])
            madre.save()
            return render(request, "App/inicio.html")
    else:
        formulario=MadreForm()
    return render(request, "App/madres.html", {'formulario':formulario})

def hermanos(request):
    
    if request.method == 'POST':
        formulario=HermanoForm(request.POST)
        if formulario.is_valid():
            informacion=formulario.cleaned_data
            hermano=Hermano(nombre=informacion['nombre'], edad=informacion['edad'])
            hermano.save()
            return render(request, "App/inicio.html")
    else:
        formulario=HermanoForm()
    return render(request, "App/hermanos.html", {'formulario':formulario})

def buscar(request):
    if request.GET['nombre']:
        nombre=request.GET['nombre']
        data1 = Padre.objects.filter(nombre=nombre)
        data2 = Madre.objects.filter(nombre=nombre)
        data3 = Hermano.objects.filter(nombre=nombre)
        data = data1.union(data2, data3)
        return render(request, "App/resultados.html", {'padres':data})
    else:
        respuesta="No se ingreso ningun nombre"
        return render(request, "App/inicio.html", {'respuesta':respuesta})
