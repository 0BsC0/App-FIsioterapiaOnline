from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    identificacion = models.CharField(max_length=20, unique=True, blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    historial_medico = models.TextField(blank=True, null=True)
    alergias = models.CharField(max_length=255, blank=True, null=True)
    medicacion_actual = models.CharField(max_length=255, blank=True, null=True)
    objetivos = models.TextField(blank=True, null=True)
    ultima_cita = models.DateField(null=True, blank=True)
    nivel_actividad = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"Perfil de {self.user.username}"
