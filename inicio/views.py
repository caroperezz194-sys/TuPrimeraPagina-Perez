from django.shortcuts import render, redirect
from django.http import HttpResponse
from inicio.models import Producto
from inicio.forms import FormularioCreacionProducto

def inicio(request):
    return render(request, 'inicio/inicio.html')

def crear_producto_v2(request):
    if request.method == "POST":
        print(request.POST)
        formulario = FormularioCreacionProducto(request.POST)
        if formulario.is_valid():
            nombre_nuevo = formulario.cleaned_data.get("nombre")
            precio_nuevo = formulario.cleaned_data.get("precio")
            
            producto = Producto(nombre=nombre_nuevo, precio=precio_nuevo)
            producto.save()
            
            return redirect("listado_productos")
        
    else:
        formulario = FormularioCreacionProducto()
    
    
    return render(request, 'inicio/crear_producto_v2.html', {'formulario': formulario})

def listado_productos(request):
    productos = Producto.objects.all()
    
    return render(request, 'inicio/listado_productos.html', {'listado_productos': productos})
