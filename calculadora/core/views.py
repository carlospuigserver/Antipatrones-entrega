from django.shortcuts import render,HttpResponse

# core/views.py

def home(request):
 return HttpResponse("<h1>Mi Web Personal</h1><h2>Portada</h2>")