from django.shortcuts import render,HttpResponse

# core/views.py

from django.shortcuts import render

def calculadora(request):
    return render(request, 'core/index.html')
