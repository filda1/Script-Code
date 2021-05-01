# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class Fila(models.Model):
    fila = models.CharField(max_length = 1)

    def __unicode__(self):
        return self.fila

class Butaca(models.Model):
    id = models.AutoField(primary_key = True)
    numero = models.CharField(max_length = 10)
    fila = models.ForeignKey(Fila)

    def __unicode__(self):
        return self.numero

class Categoria(models.Model):
    id = models.AutoField(primary_key = True)
    categoria = models.CharField(max_length = 200)

    def __unicode__(self):
        return self.categoria

class Pelicula(models.Model):
    id =  models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 255)
    nombre_alterno = models.CharField(max_length = 255,blank = True)
    duracion = models.CharField(max_length = 20)
    categoria = models.ManyToManyField(Categoria)
    fecha_estreno = models.DateField()
    idioma_original = models.CharField(max_length = 255)
    director = models.CharField(max_length = 255)
    sinopsis = models.TextField()

    def __unicode__(self):
        return '%s , %s'%(self.nombre,self.director)

class Sala(models.Model):
    id = models.AutoField(primary_key = True)
    numero = models.CharField(max_length = 2)
    tipo_sala = models.CharField(max_length = 2)
    pelicula = models.ManyToManyField(Pelicula,blank=True)
    butacas = models.ManyToManyField(Butaca,blank=True)
    cantidad_butacas = models.IntegerField()

    def __unicode__(self):
        return self.numero
