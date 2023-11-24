

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def calculadora_view(request):
    return render(request, 'calculadora/calculadora.html')