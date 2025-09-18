from django import forms

class FormularioCreacionProducto(forms.Form):
    nombre = forms.CharField(max_length=20)
    precio = forms.DecimalField(max_digits=10, decimal_places=2)
    descripcion = forms.CharField(
        widget=forms.Textarea,  
        required=False,         
        max_length=1000,        
        label='Descripción'
    )
    imagen = forms.ImageField(  
        required=False,          
        label='Imagen del producto'
    )
