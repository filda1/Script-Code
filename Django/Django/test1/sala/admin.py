# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Pelicula,Fila,Butaca,Sala,Categoria
from django.contrib import admin


admin.site.register(Pelicula)
admin.site.register(Fila)
admin.site.register(Butaca)
admin.site.register(Sala)
admin.site.register(Categoria)
