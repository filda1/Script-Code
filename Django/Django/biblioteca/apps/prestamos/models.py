from __future__ import unicode_literals

from django.db import models

class Persona(models.Model):
    dni = models.CharField(primary_key = True, max_length = 10)
    nombre = models.CharField(max_length = 100)
    apellidos = models.CharField(max_length = 120)
    numero_telefonico = models.CharField(max_length = 10)
    email = models.EmailField()
    direccion = models.CharField(max_length = 200)

    def __str__(self):
        return '%s , %s' %(self.nombre,self.apellidos)
