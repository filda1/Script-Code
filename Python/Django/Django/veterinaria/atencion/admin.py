from django.contrib import admin
from atencion.models import Persona,Tratamiento,Vacuna,Veterinario

# Register your models here.
admin.site.register(Persona)
admin.site.register(Tratamiento)
admin.site.register(Vacuna)
admin.site.register(Veterinario)
