from django.urls import path
from inicio.views import inicio, sobremi, crear_producto_v2, listado_productos, detalle_producto, EliminarProducto, ActualizarProducto
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', inicio, name='inicio'),
    path('sobremi/', sobremi, name='sobremi'),
    path('productos/crear/', crear_producto_v2, name='crear_producto'),
    path('productos/', listado_productos, name='listado_productos'),
    path('productos/detalle/<int:producto_id>/', detalle_producto, name='detalle_producto'),
    path('productos/<pk>/eliminar/', EliminarProducto.as_view(), name='eliminar_producto'),
    path('productos/<pk>/actualizar/', ActualizarProducto.as_view(), name='actualizar_producto')
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

