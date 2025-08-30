from django.urls import path
from inicio.views import inicio, crear_producto_v2, listado_productos #,crear_producto_v1

urlpatterns = [
    path('', inicio, name='inicio'),
    path('productos/crear/', crear_producto_v2, name='crear_producto'),
    path('productos/', listado_productos, name='listado_productos'),
    
]

 # path('crear-producto_v1/<nombre>/<precio>', crear_producto, name='crear_producto'),