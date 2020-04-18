# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from staff.models import Ponente
from django.db import models

class Asistente(models.Model):
	id = models.AutoField(primary_key = True)
	dni = models.CharField(unique = True,max_length = 10)
	nombre = models.CharField(max_length = 200)
	apellidos = models.CharField(max_length = 200)
	email = models.EmailField()
	direccion = models.CharField(max_length = 255)
	telefono = models.CharField(max_length = 10)

	def get_full_name(self):
		self.nombre = self.nombre+self.apellidos
		return self.nombre

	def __unicode__(self):
		return '%s , %s'%(self.nombre,self.apellidos)


class Seminario(models.Model):
	id = models.AutoField(primary_key = True)
	ponente = models.ManyToManyField(Ponente)
	tema = models.CharField(max_length = 255)
	fecha = models.DateField()
	hora_inicio = models.DateTimeField()
	hora_fin = models.DateTimeField()

	def __unicode__(self):
		return self.tema

class Evento(models.Model):
	id = models.AutoField(primary_key = True)
	seminario = models.ManyToManyField(Seminario)
	fecha_inicio = models.DateField()
	fecha_fin = models.DateField()
	asistentes = models.ManyToManyField(Asistente)

	def __unicode__(self):
		return self.id
