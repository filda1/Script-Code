from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Ponente(models.Model):
    id = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=250)
    apellidos = models.CharField(max_length=250)
    titulo = models.TextField()
    grado = models.TextField()
    lugar_trabajo = models.TextField()

    def __unicode__(self):
    	return self.nombres
