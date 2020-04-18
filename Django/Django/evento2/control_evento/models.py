from __future__ import unicode_literals
from staff.models import Ponente
from django.db import models

# Create your models here.
class Asistente(models.Model):
	id = models.AutoField(primary_key=True)
	dni = models.CharField(max_length=10)
	nombre = models.CharField(max_length=70)
	apellidos = models.CharField(max_length=200)
	email = models.EmailField()
	direccion = models.TextField()
	telefono = models.CharField(max_length=9)

	def __unicode__(self):
		return self.nombre


class Seminario(models.Model):
	id = models.AutoField(primary_key=True)
	ponente =models.ManyToManyField(Ponente)
	tema = models.CharField(max_length=80)
	fecha = models.DateField()
	fecha_inicio=models.DateTimeField()
	fecha_fin = models.DateTimeField()

	def __unicode__(self):
		return self.tema

class Evento(models.Model):
	id = models.AutoField(primary_key=True)
	seminario = models.ManyToManyField(Seminario)
	fecha_inicio=models.DateField()
	fecha_fin = models.DateField()
	asistentes = models.ManyToManyField(Asistente)

	def __unicode__(self):
		return self.id


