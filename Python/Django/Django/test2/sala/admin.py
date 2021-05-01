# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Pelicula,Sala,Fila,Categoria,Butaca
from django.contrib import admin

admin.site.register(Pelicula)
admin.site.register(Sala)
admin.site.register(Butaca)
admin.site.register(Fila)
admin.site.register(Categoria)