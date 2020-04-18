from django import forms
from .models import Seminario,Evento,Asistente


class SeminarioForm(forms.ModelForm):
	class Meta:
		model = Seminario
		fields = ['ponente','tema','fecha','hora_inicio','hora_fin',]
		labels = {'ponente':'Ponente','tema':'Tema','fecha':'Fecha',
				'hora_inicio':'Hora de inicio','hora_fin':'Hora de finalizacion',}
		widgets = {
			'ponente':forms.CheckboxSelectMultiple(),'tema':forms.TextInput(),'fecha':forms.DateInput(),
			'hora_inicio':forms.DateTimeInput(),'hora_fin':forms.DateTimeInput(),
		}		





class EventoForm(forms.ModelForm):
	class Meta:
		model = Evento
		fields = ['seminario','fecha_inicio','fecha_fin',]
		labels = {'seminario':'Seminarios','fecha_inicio':'Fecha de inicio','fecha_fin':'Fecha de finalizacion',}
		widgets = {'seminario':forms.CheckboxSelectMultiple(),'fecha_inicio':forms.DateInput(),'fecha_fin':forms.DateInput(),}



class AsistenteForm(forms.ModelForm):
	class Meta:
		model = Asistente
		fields = ['dni','nombre','apellidos','email','direccion','telefono',]
		labels = {'dni':'Dni','nombre':'Nombre','apellidos':'Apellidos','email':'Correo Electronico','direccion':'Direccion','telefono':'Telefono',}
		widgets = {'dni':forms.TextInput(),'nombre':forms.TextInput(),'apellidos':forms.TextInput(),'email':forms.TextInput()
				,'direccion':forms.TextInput(),'telefono':forms.TextInput(),}