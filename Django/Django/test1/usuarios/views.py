# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from .models import User
from .forms import UserForm,CajeroForm
from django.views.generic import CreateView,ListView,UpdateView,DeleteView

class NuevoUsuario(CreateView):
    model = User
    form_class = UserForm
    template_name = 'usuarios/nuevo_usuario.html'
    success_url = reverse_lazy('compras:listar_entrada')


def index(request):
    return render(request,'test1/base.html')


class CrearCajero(CreateView):
	model = User
	form_class = CajeroForm
	template_name = 'cajeros/crear_cajero.html'
	success_url = reverse_lazy('compras:listar_entrada')

class EditarCajero(UpdateView):
	model = User
	form_class = CajeroForm
	template_name = 'cajeros/editar_cajero.html'
	success_url = reverse_lazy('compras:listar_entrada')

class EliminarCajero(DeleteView):
	model = User
	form_class = CajeroForm
	template_name = 'cajeros/eliminar_cajero.html'
	success_url = reverse_lazy('compras:listar_entrada')

class ListarCajero(ListView):
	model = User	
	template_name = 'cajeros/listar_cajero.html'
	
