# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import Trabajador
from forms import TrabajadorForm
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy

def index(request):
    return render(request,'cinema/base.html')

class TrabajadorList(ListView):
    model = Trabajador
    template_name = 'trabajador_list.html'

class TrabajadorCreate(CreateView):
    model = Trabajador
    form_class = TrabajadorForm
    template_name = 'trabajador_create.html'
    success_url = reverse_lazy('trabajador:listar')

class TrabajadorUpdate(UpdateView):
    model = Trabajador
    form_class = TrabajadorForm
    template_name = 'trabajador_update.html'
    success_url = reverse_lazy('trabajador:listar')

class TrabajadorDelete(DeleteView):
    model = Trabajador
    template_name = 'trabajador_delete.html'
    success_url = reverse_lazy('trabajador:listar')
