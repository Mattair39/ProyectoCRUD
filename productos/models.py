from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    precio = models.FloatField()
    descripcion = models.TextField()
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.nombre)
    
