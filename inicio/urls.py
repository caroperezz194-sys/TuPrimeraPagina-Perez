from django.urls import path
from inicio.views import inicio, crear_producto_v2, sobremi, listado_productos, detalle_producto, ActualizarProducto, EliminarProducto
urlpatterns = [
    path('', inicio, name='inicio'),
    path('sobremi/', sobremi, name='sobremi'),
    path('productos/crear/', crear_producto_v2, name='crear_producto'),
    path('productos/', listado_productos, name='listado_productos'),
    path('productos/<int:producto_id>/', detalle_producto, name='detalle_producto'),
    path('productos/<pk>/actualizar/', ActualizarProducto.as_view(), name='actualizar_producto'),
    path('productos/<pk>/eliminar/', EliminarProducto.as_view(), name='eliminar_producto')
]
