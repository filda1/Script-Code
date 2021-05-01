# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.shortcuts import render
from forms import RegistroForm
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy

class RegistroUsuario(CreateView):
    model = User
    template_name = 'users/registrar.html'
    form_class = RegistroForm
    success_url = reverse_lazy('trabajador:index')
