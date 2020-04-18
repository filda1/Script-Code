from __future__ import unicode_literals

from django.db import models

class Usuario(models.Model):
	nombre = models.CharField(max_length = 255)
	apellidos = models.CharField(max_length = 255)
	direccion = models.CharField(max_length = 255)
	telefono = models.CharField(max_length = 255)
	mascota = models.CharField(max_length = 255)
	image = models.URLField(null = True, blank = True)

	def __unicode__(self):
		return self.nombre
