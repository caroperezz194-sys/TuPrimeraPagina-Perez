from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=20)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField(blank=True)
    
    def __str__(self):
        return f"Nombre: {self.nombre} - Precio: {self.precio}"