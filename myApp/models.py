from django.db import models

class Empresa(models.Model):
    nombre = models.CharField(max_length=50)
    cif = models.CharField(max_length=12)

class Trabajador(models.Model):
    #Campo para la relación

    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=40)
    fecha_nacimiento = models.DateField()

    #Es posible indicar un valor por defecto mediante default de
    antiguedad = models.IntegerField(default=0)

    