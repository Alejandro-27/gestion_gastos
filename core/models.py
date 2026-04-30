from django.db import models
from django.contrib.auth.models import User



class Gastos(models.Model):
    # Esto vincula el gasto al usuario que inició sesión
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) 
    descripcion = models.CharField(max_length=200)
    monto = models.DecimalField(max_digits=12, decimal_places=2) 
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.username} - {self.descripcion}"