# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Seminario,Evento,Asistente
from django.shortcuts import render
from .forms import SeminarioForm,EventoForm,AsistenteForm
from django.views.generic import CreateView,DeleteView,UpdateView,ListView
from django.core.urlresolvers import reverse_lazy
#Importamos settings para poder tener a la mano la ruta de la carpeta media
from django.conf import settings
from io import BytesIO
from reportlab.pdfgen import canvas
from django.views.generic import View
from django.http import HttpResponse
from reportlab.platypus import Table,TableStyle
from reportlab.lib.units import cm
from reportlab.lib import colors

class CrearAsistente(CreateView):
    model = Asistente
    form_class = AsistenteForm
    template_name = 'asistente/crear_asistente.html'
    success_url = reverse_lazy('evento:listar_asistente')

class ListarAsistente(ListView):
    model = Asistente
    template_name = 'asistente/listar_asistente.html'

class EditarAsistente(UpdateView):
    model = Asistente
    form_class = AsistenteForm
    template_name = 'asistente/editar_asistente.html'
    success_url = reverse_lazy('evento:listar_asistente')

class EliminarAsistente(DeleteView):
    model = Asistente
    form_class = AsistenteForm
    template_name = 'asistente/eliminar_asistente.html'
    success_url = reverse_lazy('evento:listar_asistente')

#############################################


class CrearSeminario(CreateView):
    model = Seminario
    form_class = SeminarioForm
    template_name = 'seminario/crear_seminario.html'
    success_url = reverse_lazy('evento:listar_seminario')

class ListarSeminario(ListView):
    model = Seminario
    template_name = 'seminario/listar_seminario.html'

class EditarSeminario(UpdateView):
    model = Seminario
    form_class = SeminarioForm 
    template_name = 'seminario/editar_seminario.html'
    success_url = reverse_lazy('evento:listar_seminario')

class EliminarSeminario(DeleteView):
    model = Seminario
    form_class = SeminarioForm
    template_name = 'seminario/eliminar_seminario.html'
    success_url = reverse_lazy('evento:listar_seminario')


#############################################

class CrearEvento(CreateView):
    model = Evento
    form_class = EventoForm
    template_name = 'evento/crear_evento.html'
    success_url = reverse_lazy('evento:listar_evento')

class ListarEvento(ListView):
    model = Evento
    template_name = 'evento/listar_evento.html'

class EditarEvento(UpdateView):
    model = Evento
    form_class = EventoForm
    template_name = 'evento/editar_evento.html'
    success_url = reverse_lazy('evento:listar_evento')

class EliminarEvento(DeleteView):
    model = Evento
    form_class = EventoForm
    template_name = 'evento/eliminar_evento.html'
    success_url = reverse_lazy('evento:listar_evento')



class ReportePersonasPDF(View):
    def cabecera(self,pdf):
            #Utilizamos el archivo logo_django.png que está guardado en la carpeta media/imagenes
            #archivo_imagen = settings.MEDIA_ROOT+'/imagenes/logo_django.png'
            #Definimos el tamaño de la imagen a cargar y las coordenadas correspondientes
           # pdf.drawImage(archivo_imagen, 40, 750, 120, 90,preserveAspectRatio=True)
            #Establecemos el tamaño de letra en 16 y el tipo de letra Helvetica
            pdf.setFont("Helvetica", 16)
            #Dibujamos una cadena en la ubicación X,Y especificada
            pdf.drawString(180, 790, u"Reporte de Asistentes a Evento")
            pdf.setFont("Helvetica", 14)            
            pdf.drawString(200, 760, u"REPORTE DE PERSONAS")

    def tabla(self,pdf,y):
        #Creamos una tupla de encabezados para nuestra tabla
        encabezados = ('DNI', 'Nombre', 'Apellidos', 'Email', 'Telefono')
        #Creamos una lista de tuplas que van a contener a las personas
        detalles = [(persona.dni, persona.nombre,persona.apellidos, persona.email, persona.telefono) 
                        for persona in Asistente.objects.all()]
        #Establecemos el tamaño de cada una de las columnas de la tabla
        detalle_orden = Table([encabezados] + detalles, colWidths=[2 * cm, 2 * cm, 3 * cm, 5 * cm, 3 * cm])
        #Aplicamos estilos a las celdas de la tabla
        detalle_orden.setStyle(TableStyle(
        [
                #La primera fila(encabezados) va a estar centrada
                ('ALIGN',(0,0),(3,0),'CENTER'),
                #Los bordes de todas las celdas serán de color negro y con un grosor de 1
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
                #El tamaño de las letras de cada una de las celdas será de 10
                ('FONTSIZE', (0, 0), (-1, -1), 10),
                ]
        ))
        #Establecemos el tamaño de la hoja que ocupará la tabla
        detalle_orden.wrapOn(pdf, 800, 600)
        #Definimos la coordenada donde se dibujará la tabla        
        detalle_orden.drawOn(pdf, 80,y)


    def get(self, request, *args, **kwargs):
            #Indicamos el tipo de contenido a devolver, en este caso un pdf
            response = HttpResponse(content_type='application/pdf')
            #La clase io.BytesIO permite tratar un array de bytes como un fichero binario, se utiliza como almacenamiento temporal
            buffer = BytesIO()
            #Canvas nos permite hacer el reporte con coordenadas X y Y
            pdf = canvas.Canvas(buffer)
            #Llamo al método cabecera donde están definidos los datos que aparecen en la cabecera del reporte.
            self.cabecera(pdf)
            y = 30
            self.tabla(pdf, y)
            #Con show page hacemos un corte de página para pasar a la siguiente
            pdf.showPage()
            pdf.save()
            pdf = buffer.getvalue()
            buffer.close()
            response.write(pdf)
            return response