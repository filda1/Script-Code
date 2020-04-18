# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Asistente,Evento,Seminario
from django.contrib import admin


admin.site.register(Asistente)
admin.site.register(Evento)
admin.site.register(Seminario)