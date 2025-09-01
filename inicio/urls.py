from django.urls import path
from inicio.views import inicio, crear_producto_v2, listado_productos, borrar_producto

urlpatterns = [
    path('', inicio, name='inicio'),
    path('productos/crear/', crear_producto_v2, name='crear_producto'),
    path('productos/', listado_productos, name='listado_productos'),
    path('productos/borrar/<int:producto_id>/', borrar_producto, name='borrar_producto'),

]
