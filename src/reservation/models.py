from django.db import models

# Create your models here.

class Reservation(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    numero_de_telefono = models.IntegerField()
    numero_de_personas = models.IntegerField()
    fecha = models.DateField()
    hora = models.TimeField()
    
    class Meta:
        verbose_name = 'reservacion'
        verbose_name_plural = 'reservaciones'


    def __str__(self):
        return self.nombre