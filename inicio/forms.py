from django import forms

class FormularioCreacionProducto(forms.Form):
    nombre = forms.CharField(max_length=20)
    precio = forms.DecimalField(max_digits=10, decimal_places=2)