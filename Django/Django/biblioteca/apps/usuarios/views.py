from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from .forms import UserForm

class CrearUsuario(CreateView):
	model = User
	form_class = UserForm
	template_name = 'usuarios/crear_usuario.html'
	success_url = reverse_lazy('libros:listar_libro')