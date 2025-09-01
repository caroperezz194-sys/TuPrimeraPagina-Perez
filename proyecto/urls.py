"""
URL configuration for proyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from inicio.views import inicio, crear_producto_v2, listado_productos, borrar_producto #,crear_producto_v1

urlpatterns = [
    path('', inicio, name='inicio'),
    path('productos/crear/', crear_producto_v2, name='crear_producto'),
    path('productos/', listado_productos, name='listado_productos'),
    path('productos/borrar/<int:producto_id>/', borrar_producto, name='borrar_producto'),


    
]
# path('productos/borrar/<int:producto_id>/', borrar_producto, name='borrar_producto')