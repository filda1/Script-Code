# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Ponente(models.Model):
	id = models.AutoField(primary_key = True)
	nombre = models.CharField(max_length = 255)
	apellidos = models.CharField(max_length = 255)
	dni = models.CharField(max_length = 10)
	email = models.EmailField()
	grados = models.TextField()
	titulos = models.TextField()
	lugares_trabajo = models.TextField()

	def __unicode__(self):
		return '%s , %s'%(self.nombre,self.apellidos)



