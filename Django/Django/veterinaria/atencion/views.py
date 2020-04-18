from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import ListView,CreateView,DeleteView,UpdateView
from django.core.urlresolvers import reverse_lazy
from models import Persona,Veterinario,Vacuna
from forms import PersonaForm,VeterinarioForm

class PersonaList(ListView):
	model=Persona
	template_name='atencion/persona_list.html'

class PersonaCreate(CreateView):
	model = Persona
	form_class = PersonaForm
	template_name= 'atencion/persona_form.html'
	success_url=reverse_lazy('atencion:persona_list')

class PersonaDelete(DeleteView):
	model = Persona
	form_class = PersonaForm
	template_name= 'atencion/persona_delete.html'
	success_url=reverse_lazy('atencion:persona_list')

class PersonaUpdate(UpdateView):	
	model = Persona
	form_class = PersonaForm
	template_name= 'atencion/persona_form.html'
	success_url=reverse_lazy('atencion:persona_list')


#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------

class VeterinarioList(ListView):
	model=Veterinario
	template_name='atencion/veterinario_list.html'

class VeterinarioCreate(CreateView):
	model= Veterinario
	form_class=VeterinarioForm
	template_name='atencion/veterinario_form.html'
	success_url=reverse_lazy('atencion:veterinario_list')

class VeterinarioUpdate(UpdateView):
	model= Veterinario
	form_class=VeterinarioForm
	template_name='atencion/veterinario_form.html'
	success_url=reverse_lazy('atencion:veterinario_list')

class VeterinarioDelete(DeleteView):
	model= Veterinario
	form_class=VeterinarioForm
	template_name='atencion/veterinario_delete.html'
	success_url=reverse_lazy('atencion:veterinario_list')