from django.shortcuts import render, redirect
from inicio.models import Producto
from inicio.forms import FormularioCreacionProducto
from django.shortcuts import get_object_or_404
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

def inicio(request):
    return render(request, 'inicio/inicio.html')

@login_required
def crear_producto_v2(request):
    if request.method == "POST":
        print(request.POST)
        formulario = FormularioCreacionProducto(request.POST)
        if formulario.is_valid():
            nombre_nuevo = formulario.cleaned_data.get("nombre")
            precio_nuevo = formulario.cleaned_data.get("precio")
            descripcion_nueva = formulario.cleaned_data.get("descripcion")
            
            producto = Producto(nombre=nombre_nuevo, 
                                precio=precio_nuevo, 
                                descripcion=descripcion_nueva)
            producto.save()
            
            return redirect("listado_productos")
        
    else:
        formulario = FormularioCreacionProducto()
    
    
    return render(request, 'inicio/crear_producto_v2.html', {'formulario': formulario})

def listado_productos(request):
    productos = Producto.objects.all()
    
    return render(request, 'inicio/listado_productos.html', {'listado_productos': productos})

def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    return render(request, 'inicio/detalle_producto.html', {'producto': producto})

def sobremi(request):
    return render(request, 'inicio/sobremi.html')

class ActualizarProducto(LoginRequiredMixin, UpdateView):
    model = Producto
    template_name = "inicio/actualizar_producto.html"
    fields = '__all__'
    success_url = reverse_lazy("listado_productos")
    

class EliminarProducto(LoginRequiredMixin, DeleteView):
    model = Producto
    template_name = "inicio/eliminar_producto.html"
    success_url = reverse_lazy("listado_productos")










