from django.shortcuts import render
from django.views.generic import CreateView,DeleteView,UpdateView,ListView
from django.core.urlresolvers import reverse_lazy
from .models import Ponente
from .forms import PonenteForm

class CrearPonente(CreateView):
    model = Ponente
    form_class = PonenteForm
    template_name = 'ponente/crear_ponente.html'
    success_url = reverse_lazy('ponente:listar_ponente')
    
class ListarPonente(ListView):
    model = Ponente
    template_name = 'ponente/listar_asistente.html'
    
class EditarPonente(UpdateView):
    model = Ponente
    form_class = PonenteForm
    template_name = 'ponente/editar_ponente.html'
    success_url = reverse_lazy('ponente:listar_ponente')
    
class EliminarPonente(DeleteView):
    model = Ponente
    form_class = PonenteForm
    template_name = 'ponente/eliminar_ponente.html'
    success_url = reverse_lazy('ponente:listar_ponente')