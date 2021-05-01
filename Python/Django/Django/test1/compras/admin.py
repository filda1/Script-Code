# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Entrada,Funcion,TipoEntrada
from django.contrib import admin

admin.site.register(Entrada)
admin.site.register(Funcion)
admin.site.register(TipoEntrada)
