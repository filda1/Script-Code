from __future__ import unicode_literals
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.views.generic import CreateView,DeleteView,UpdateView,ListView
from .models import Pelicula,Sala
from .forms import PeliculaForm,SalaForm

#####################################################
#PELICULA

class CrearPelicula(CreateView):
    model = Pelicula
    form_class = PeliculaForm
    template_name = 'pelicula/crear_pelicula.html'
    success_url = reverse_lazy('sala:listar_pelicula')

class ListarPelicula(ListView):
    model = Pelicula
    template_name = 'pelicula/listar_pelicula.html'

class EditarPelicula(UpdateView):
    model = Pelicula
    form_class = PeliculaForm
    template_name = 'pelicula/editar_pelicula.html'
    success_url = reverse_lazy('sala:listar_pelicula')

class EliminarPelicula(DeleteView):
    model = Pelicula
    form_class = PeliculaForm
    template_name = 'pelicula/eliminar_pelicula.html'
    success_url = reverse_lazy('sala:listar_pelicula')


#######################################################
#SALA

class CrearSala(CreateView):
    model = Sala
    form_class = SalaForm
    template_name = 'sala/crear_sala.html'
    success_url = reverse_lazy('sala:listar_sala')


class ListarSala(ListView):
    model = Sala
    template_name = 'sala/listar_sala.html'

class EditarSala(UpdateView):
    model = Sala
    form_class = SalaForm
    template_name = 'sala/editar_sala.html'
    success_url = reverse_lazy('sala:listar_sala')


class EliminarSala(DeleteView):
    model = Sala
    form_class = SalaForm
    template_name = 'sala/eliminar_sala.html'
    success_url = reverse_lazy('sala:listar_sala')
