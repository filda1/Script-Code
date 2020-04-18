# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Pelicula,CategoriaPelicula,RestriccionesPelicula

admin.site.register(Pelicula)
admin.site.register(CategoriaPelicula)
admin.site.register(RestriccionesPelicula)
