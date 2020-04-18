from django.contrib import admin
from .models import Evento,Asistente,Seminario

admin.site.register(Evento)
admin.site.register(Seminario)
admin.site.register(Asistente)
