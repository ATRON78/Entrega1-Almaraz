from django.shortcuts import render
from .models import *
from django.http import HttpResponse

# Create your views here.

def padre(request):
    padre=Padre(nombre="Adrian", edad=44)
    padre.save()
    return HttpResponse(f"Mi padre se llama {padre.nombre}")