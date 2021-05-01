from django.shortcuts import render,redirect
from .forms import LibroForm
from .models import Libro
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy

def home(request):
    return render(request,'base/base.html')

def create_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('libros:home')
    else:
        form = LibroForm()

    return render(request,'libros/crear_libro.html',{'form':form})

def list_libro(request):
	libro = Libro.objects.all() # select * from libro
	contexto = {'libros':libro}
	return render(request,'libros/listar_libro.html',contexto)

def edit_libro(request,codigo):
	libro = Libro.objects.get(codigo = codigo)
	if request.method == 'GET':
		form = LibroForm(instance = libro)
	else:
		form = LibroForm(request.POST , instance = libro)
		if form.is_valid():
			form.save()
		return redirect('libros:listar_libro')
	return render(request,'libros/editar_libro.html',{'form':form })

def delete_libro(request,codigo):
	libro = Libro.objects.get(codigo = codigo)
	if request.method == 'POST':
		libro.delete()
		return redirect('libros:listar_libro')
	return render(request,'libros/eliminar_libro.html',{'libro':libro})


class ListarView(ListView):
	model = Libro
	template_name = 'base/base.html'

class CrearView(CreateView):
	model = Libro
	form_class = LibroForm
	template_name = 'libros/crear_libro.html'
	success_url = reverse_lazy('libros:listar_libro')

class EditarView(UpdateView):
	model = Libro
	form_class = LibroForm
	template_name = 'libros/editar_libro.html'
	success_url = reverse_lazy('libros:listar_libro')

class EliminarView(DeleteView):
	model = Libro
	form_class = LibroForm
	template_name = 'libros/eliminar_libro.html'
	success_url = reverse_lazy('libros:listar_libro')