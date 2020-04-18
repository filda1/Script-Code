from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from forms import RegistroForm

class RegistroUsuario(CreateView):
	model = User
	template_name = "usuario/nuevo.html"
	form_class = RegistroForm
	success_url = reverse_lazy('mascota:home_mascota')