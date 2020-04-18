# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from tipo_usuario.models import Tipo_Usuario

class Trabajador(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    username = models.CharField(max_length=20)
    area = models.CharField(max_length=45)
    dni = models.CharField(max_length=15, unique=True)
    email = models.EmailField(max_length=200)
    sexo = models.CharField(max_length=40)
    tipo_usuario = models.ForeignKey(Tipo_Usuario, on_delete=models.CASCADE)

    class Meta:
        ordering = ["id"]
