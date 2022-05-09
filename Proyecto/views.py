from django.http import HttpResponse
from django.template import Template, Context, loader

def saludo(request):
    return HttpResponse("Hola Mundo")

def probando_template(request):

    lista_de_nombres=["Juan","Pedro","Ana","Maria","Luis"]

    diccionario={"lista":lista_de_nombres, "clase":"Curso de django"}

    plantilla=loader.get_template("inicio.html")
    
    documento=plantilla.render(diccionario)
    return HttpResponse(documento)