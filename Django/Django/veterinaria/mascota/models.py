from __future__ import unicode_literals

from django.db import models
from atencion.models import Persona,Tratamiento,Vacuna


class Mascota(models.Model):
	nombre=models.CharField(max_length=60)
	sexo=models.CharField(max_length=25)
	edad_aproximada=models.IntegerField()
	fecha_obtencion=models.DateField()
	persona=models.ForeignKey(Persona,null=True,blank=True,on_delete=models.CASCADE)

	def __unicode__(self):
		return '{}'.format(self.nombre)