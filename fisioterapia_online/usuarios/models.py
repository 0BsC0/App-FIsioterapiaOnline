from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    identificacion = models.CharField(max_length=20, unique=True, db_column='Identificacion')
    telefono = models.CharField(max_length=15, null=True, blank=True, db_column='Telefono')
    email = models.EmailField(unique=True, db_column='Correo')  # Maps to 'Correo'
    password = models.CharField(max_length=255, db_column='Contraseña')  # Maps to 'Contraseña'
    fecha_nacimiento = models.DateField(null=True, blank=True, db_column='Fecha_Nacimiento')
    fecha_registro = models.DateTimeField(auto_now_add=True, db_column='Fecha_Registro')

    # Map the default relations for groups and permissions
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='usuarios_groups',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='usuarios_permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Cita(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, db_column='ID_Usuario')
    fecha_cita = models.DateField(db_column='Fecha_Cita')
    hora_cita = models.TimeField(db_column='Hora_Cita')
    estado_asistencia = models.CharField(
        max_length=10,
        choices=[('Asistió', 'Asistió'), ('No asistió', 'No asistió')],
        default='No asistió',
        db_column='Estado_Asistencia'
    )

    def __str__(self):
        return f"Cita de {self.usuario} el {self.fecha_cita} a las {self.hora_cita}"
