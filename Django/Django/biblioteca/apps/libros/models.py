from __future__ import unicode_literals

from django.db import models

class Autor(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 255)
    apellidos = models.CharField(max_length = 255)
    direccion = models.CharField(max_length = 255)
    email = models.EmailField()

    def __str__(self):
        return self.nombre


class Libro(models.Model):
    codigo = models.AutoField(primary_key = True)
    titulo = models.CharField(max_length = 255)
    autor = models.ManyToManyField(Autor)
    descripcion = models.TextField()
    editorial = models.CharField(max_length = 70)
    fecha_publicacion = models.DateField()
    numero_paginas = models.IntegerField()

    def __str__(self):
        return self.titulo
