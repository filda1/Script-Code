from django.shortcuts import render
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from .models import User
from .forms import UserForm


class CrearUsuario(CreateView):
    model = User
    form_class = UserForm
    template_name = 'usuarios/crear_usuario.html'
    success_url = reverse_lazy('index')


def home(request):
	return render(request,'usuarios/base.html')




