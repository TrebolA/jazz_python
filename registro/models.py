from django.db import models
from django.utils import timezone

class Registro(models.Model):
    CIUDADES = (
        ('Bg', 'Bogotá'),
        ('Md', 'Medellín'),
    )

    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    correo = models.EmailField()
    celular = models.BigIntegerField()
    ciudad = models.CharField(
        max_length=2,
        choices=CIUDADES,
        default='Bg',
    )
    terminos = models.BooleanField()
    politica = models.BooleanField()
    #codigo = models.CharField(max_length=10, null=True)
