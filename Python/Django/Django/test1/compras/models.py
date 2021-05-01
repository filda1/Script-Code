# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from sala.models import Pelicula,Sala

class TipoEntrada(models.Model):
    id = models.AutoField(primary_key = True)
    tipo = models.CharField(max_length = 255)

    def __unicode__(self):
        return self.tipo

class Entrada(models.Model):
    id = models.AutoField(primary_key = True)
    hora_compra = models.TimeField()
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits = 10, decimal_places = 4,default = 7,blank = True)
    tipo_entrada = models.ManyToManyField(TipoEntrada)
    total_pagado = models.DecimalField(max_digits = 10,decimal_places = 4,default = 0)
    sala = models.ForeignKey(Sala)
    pelicula = models.ForeignKey(Pelicula)

    def vuelto(self):
        vuelto = self.total_pagado-(self.cantidad*self.precio)
        return vuelto

    def __unicode__(self):
        return str(self.id)

class Funcion(models.Model):
    id = models.AutoField(primary_key = True)
    hora_funcion = models.TimeField()
    pelicula = models.ManyToManyField(Pelicula)
    sala = models.ForeignKey(Sala)

    def __unicode__(self):
        return str(self.id)
