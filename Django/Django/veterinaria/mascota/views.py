from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import ListView,CreateView,DeleteView,UpdateView
from django.core.urlresolvers import reverse_lazy
from forms import MascotaForm
from models import Mascota

class MascotaList(ListView):
	model = Mascota	
	template_name='mascota/home.html'
	

class MascotaCreate(CreateView):
	model = Mascota
	form_class=MascotaForm
	template_name='mascota/mascota_form.html'
	success_url=reverse_lazy('mascota:home_mascota')

class MascotaUpdate(UpdateView):
	model=Mascota
	form_class=MascotaForm
	template_name='mascota/mascota_form.html'
	success_url=reverse_lazy('mascota:home_mascota')


class MascotaDelete(DeleteView):
	model=Mascota
	form_class=MascotaForm
	template_name='mascota/mascota_delete.html'
	success_url=reverse_lazy('mascota:home_mascota')


#--------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------


