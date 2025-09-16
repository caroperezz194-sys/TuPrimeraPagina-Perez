from django import forms

class FormularioCreacionProducto(forms.Form):
    nombre = forms.CharField(max_length=20)
    precio = forms.DecimalField(max_digits=10, decimal_places=2)
    descripcion = forms.CharField(
        widget=forms.Textarea,  # permite escribir varias líneas
        required=False,         # opcional si quieres permitir que quede vacío
        max_length=1000,        # límite de caracteres (puedes ajustar)
        label='Descripción'
    )