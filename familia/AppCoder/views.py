from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from .models import Family

def family(request, nombre, edad, nacimiento):

    family = Family(nombre=nombre, edad=edad, nacimiento= nacimiento)
    family.save()
    return HttpResponse(f""" <p>{family.nombre} de edad {family.edad} y su nacimiento es {family.nacimiento}""")

def lista_family(request):
    
    lista=Family.objects.all()
    
    return render(request, "familiares.html", {"familiares": lista})

