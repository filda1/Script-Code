# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from django.shortcuts import render
from .models import CategoriaPelicula,RestriccionesPelicula,Pelicula
from .forms import CategoriaPeliculaForm,PeliculaForm,RestriccionesPeliculaForm
from django.core.urlresolvers import reverse_lazy


class CrearCategoriaPeliculaView(CreateView):
    model = CategoriaPelicula
    form_class = CategoriaPeliculaForm
    template_name = 'pelicula/categoria/crear_categoria.html'
    success_url = reverse_lazy('pelicula:listar_categoria')

class ListarCategoriaPeliculaView(ListView):
    model = CategoriaPelicula
    template_name = 'pelicula/categoria/listar_categoria.html'

class EditarCategoriaPeliculaView(UpdateView):
    model = CategoriaPelicula
    form_class = CategoriaPeliculaForm
    template_name = 'pelicula/categoria/actualizar_categoria.html'
    success_url = reverse_lazy('pelicula:listar_categoria')

class EliminarCategoriaPeliculaView(DeleteView):
    model = CategoriaPelicula
    form_class = CategoriaPeliculaForm
    template_name = 'pelicula/categoria/eliminar_categoria.html'
    success_url = reverse_lazy('pelicula:listar_categoria')




class CrearRestricciones(CreateView):
    model = RestriccionesPelicula
    form_class = RestriccionesPeliculaForm
    template_name = 'pelicula/restriccion/crear_restricciones.html'
    success_url = reverse_lazy('pelicula:listar_restricciones')

class ListarRestricciones(ListView):
    model = RestriccionesPelicula
    template_name = 'pelicula/restriccion/listar_restricciones.html'

class EditarRestricciones(UpdateView):
    model = RestriccionesPelicula
    form_class = RestriccionesPeliculaForm
    template_name = 'pelicula/restriccion/actualizar_restricciones.html'
    success_url = reverse_lazy('pelicula:listar_restricciones')

class EliminarRestricciones(DeleteView):
    model = RestriccionesPelicula
    form_class = RestriccionesPeliculaForm
    template_name = 'pelicula/restriccion/eliminar_restricciones.html'
    success_url = reverse_lazy('pelicula:listar_restricciones')


class CrearPelicula(CreateView):
    model = Pelicula
    form_class = PeliculaForm
    template_name = 'pelicula/crear_pelicula.html'
    success_url = reverse_lazy('pelicula/listar_peliculas')

class ListarPelicula(ListView):
    model = Pelicula
    template_name = 'pelicula/listar_peliculas.html'

class EditarPelicula(UpdateView):
    model = Pelicula
    form_class = PeliculaForm
    template_name = 'pelicula/actualizar_pelicula.html'
    success_url = reverse_lazy('pelicula:listar_peliculas')

class EliminarPelicula(DeleteView):
    model = Pelicula
    form_class = PeliculaForm
    template_name = 'pelicula/eliminar_pelicula.html'
    success_url = reverse_lazy('pelicula:listar_peliculas')
