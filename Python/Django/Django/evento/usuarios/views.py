# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .forms import UserForm
from django.shortcuts import render
from .models import User
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.forms import UserCreationForm

class UserCreate(CreateView):
	model = User	
	form_class = UserForm
	template_name = 'usuarios/crear_usuario.html'
	success_url = reverse_lazy('index')

def home(request):
	return render(request,'usuarios/base.html')

