from django.shortcuts import render,redirect
from .forms import UsuarioForm

def home(request):
	return render(request,'index.html')

def nosotros(request):
	return render(request,'nosotros.html')

def servicios(request):
	return render(request,'servicios.html')

def servicios_premium(request):
	return render(request,'servicio_premium.html')

def contactanos(request):
	return render(request,'contactanos.html')

def acceder(request):
	return render(request,'acceder.html')

def urnas(request):
	return render(request,'urnas.html')

def urnas2(request):
	return render(request,'urnas2.html')

def urnas3(request):
	return render(request,'urnas3.html')

def urnas4(request):
	return render(request,'urnas4.html')

def urnas5(request):
	return render(request,'urnas5.html')

def urnas6(request):
	return render(request,'urnas6.html')

def registro(request):
	if request.method == 'POST':
		form = UsuarioForm(request.POST or None, request.FILES or None)
		if form.is_valid():
			form.save()
			return redirect('urnas')		
	else:
		form = UsuarioForm()

	return render(request,'registro.html',{'form':form})


