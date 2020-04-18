# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Entrada
from .forms import EntradaForm
from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView,ListView,DeleteView,UpdateView

class NuevaEntrada(CreateView):
    model = Entrada
    form_class = EntradaForm
    template_name = 'compras/nueva_entrada.html'
    success_url = reverse_lazy('compras:listar_entrada')

class ListarEntrada(ListView):
    model = Entrada
    template_name = 'compras/listar_entrada.html'

class EditarEntrada(UpdateView):
    model = Entrada
    form_class = EntradaForm
    template_name = 'compras/editar_entrada.html'
    success_url = reverse_lazy('compras:listar_entrada')

class EliminarEntrada(DeleteView):
    model = Entrada
    form_class = EntradaForm
    template_name = 'compras/eliminar_entrada.html'
    success_url = reverse_lazy('compras:listar_entrada')
