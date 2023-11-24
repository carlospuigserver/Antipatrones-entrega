from django.shortcuts import render
from django.http import HttpResponse
from .forms import CalculatorForm

def calculator(request):
    form = CalculatorForm()

    if request.method == 'POST':
        form = CalculatorForm(request.POST)
        if form.is_valid():
            expression = form.cleaned_data['expression']
            try:
                result = eval(expression)
                form.cleaned_data['expression'] = str(result)
            except Exception as e:
                form.add_error('expression', f"Error en la expresión: {str(e)}")

    return render(request, 'core/calculator.html', {'form': form})