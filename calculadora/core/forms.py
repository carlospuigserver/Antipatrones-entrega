# core/forms.py
from django import forms

class CalculatorForm(forms.Form):
    expression = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly', 'class': 'form-control', 'id': 'expression'}))
