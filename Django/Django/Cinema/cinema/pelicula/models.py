# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class CategoriaPelicula(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=60)

    def __unicode__(self):
        return self.nombre

class RestriccionesPelicula(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40)
    observaciones = models.TextField()

    def __unicode__(self):
        return self.nombre

class Pelicula(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length = 255)
    nombre_alterno = models.CharField(max_length = 255)
    duracion = models.CharField( max_length = 50)
    director = models.CharField( max_length = 255)
    elenco = models.TextField()
    grupo_produccion = models.TextField()
    fecha_estreno = models.DateField()
    idioma = models.CharField(max_length = 50)
    pais = models.CharField(max_length = 50)
    distribuidora = models.CharField(max_length = 70)
    descripcion = models.TextField()
    restricciones_pelicula = models.ForeignKey(RestriccionesPelicula, on_delete =models.CASCADE)
    categoria_pelicula = models.ManyToManyField(CategoriaPelicula)

    def __unicode__(self):
        return self.nombre

    class Meta:
        ordering = ['fecha_estreno']
