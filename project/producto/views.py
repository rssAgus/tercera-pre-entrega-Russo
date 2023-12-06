from django.shortcuts import render
from cliente import models

def home(request):
    return render(request, "producto/index.html")

def view_guitarras(request):
    guitarra = models.Guitarras.objects.all()
    context = {"Guitarra" : guitarra}
    return render(request, "Producto/ver_guitarras.html", context)
