from django.db import models

# Create your models here.

class Reservas(models.Model):
    responsable = models.CharField(max_length=80, null=False)
    telefono = models.IntegerField(max_length=15,null=False)
    fechaReserva = models.DateField(null=False)
    horaReserva = models.TimeField(null=False)
    cantidadPersonas = models.IntegerField(null=False)
    email = models.EmailField(max_length=80 ,null=False)
    estado = models.CharField(max_length=15, null=False)
    observacion = models.CharField(max_length=255)