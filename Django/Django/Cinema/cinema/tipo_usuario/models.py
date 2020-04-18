# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Tipo_Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=50)
