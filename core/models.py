from django.db import models
from django.contrib.auth.models import User

class Gastos(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) 
    descripcion = models.CharField(max_length=200)
    monto = models.DecimalField(max_digits=12, decimal_places=2) 
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Si el usuario es None (invitado)
        nombre_usuario = self.usuario.username if self.usuario else "Invitado"
        return f"{nombre_usuario} - {self.descripcion}"