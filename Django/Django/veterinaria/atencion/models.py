from __future__ import unicode_literals

from django.db import models

class Persona(models.Model):
	dni=models.CharField(max_length=12,primary_key=True)
	nombre=models.CharField(max_length=150)
	apellidos=models.CharField(max_length=150)
	edad=models.IntegerField()
	telefono=models.CharField(max_length=12)
	email=models.EmailField()
	domicilio=models.CharField(max_length=200)

	def __unicode__(self):
		return '{}'.format(self.nombre,self.apellidos)

class Veterinario(models.Model):
	codigomedico=models.CharField(max_length=12,primary_key=True)
	dni=models.CharField(max_length=12)
	nombre=models.CharField(max_length=150)
	apellidos=models.CharField(max_length=150)
	fecha_nacimiento=models.DateField()
	telefono=models.CharField(max_length=12)
	email=models.EmailField()
	domicilio=models.CharField(max_length=200)
	fecha_contratacion=models.DateField()
	horario=models.TextField()

	def __unicode__(self):
		return '{}'.format(self.codigomedico,self.nombre,self.apellidos)

class Tratamiento(models.Model):
	nombre=models.CharField(max_length=150)
	descripcion=models.TextField()
	vete=models.ForeignKey(Veterinario,null=True,blank=True,on_delete=models.CASCADE)
	def __unicode__(self):
		return '{}'.format(self.nombre)

class Vacuna(models.Model):
	nombre=models.CharField(max_length=150)
	descripcion=models.TextField()

	def __unicode__(self):
		return '{}'.format(self.nombre)

class Solicitd(models.Model):
	persona = models.ForeignKey(Persona,null=False,blank=False)
	veterinario=models.ForeignKey(Veterinario,null=False,blank=False)
	vacuna=models.ForeignKey(Vacuna,null=False,blank=False)
	fecha=models.DateField()
