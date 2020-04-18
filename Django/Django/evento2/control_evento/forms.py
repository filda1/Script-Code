from django import forms
from .models import Asistente,Seminario,Evento


class AsistenteForm(forms.ModelForm):
	class Meta:
		model = Asistente
		fields = [
		'dni',
		'nombre',
		'apellidos',
		'email',
		'direccion',
		'telefono',
		]

		labels={
		'dni':'DNI',
		'nombre':'Nombre',
		'apellidos':'Apellidos',
		'email':'Email',
		'direccion':'Direccion',
		'telefono':'Telefono',
		}
		widgets={
		'dni':forms.TextInput(),
		'nombre':forms.TextInput(),
		'apellidos':forms.TextInput(),
		'email': forms.TextInput(),
		'direccion': forms.TextInput(),
		'telefono': forms.TextInput(),
		}


class SeminarioForm(forms.ModelForm):
	class Meta:
		model = Seminario
		fields = [
		'ponente',
		'tema',
		'fecha',
		'fecha_inicio',
		'fecha_fin',
		]

		labels={
		'ponente':'Ponente',
		'tema':'Tema',
		'fecha':'Fecha',
		'fecha_inicio': 'Fecha de Inicio',
		'fecha_fin': 'Fecha Fin',
		}

		widgets={
		'ponente':forms.CheckboxSelectMultiple(),
		'tema':forms.TextInput(),
		'fecha':forms.DateInput(),
		'fecha_inicio':forms.DateTimeInput(),
		'fecha_fin':forms.DateTimeInput(),
		}

class EventoForm(forms.ModelForm):
	class Meta:
		model = Evento
		fields = [
			'seminario',
			'fecha_inicio',
			'fecha_fin',
			'asistentes',
		]

		labels={
			'seminario':'Seminario',
			'fecha_inicio':'Fecha de Incio',
			'fecha_fin': 'Fecha de Finalizacion',
			'asistentes':'Asistentes',
		

		}
		widgets={
			'seminario':forms.CheckboxSelectMultiple(),
			'fecha_inicio':forms.DateTimeInput(),
			'fecha_fin':forms.DateTimeInput(),
			'asistentes':forms.CheckboxSelectMultiple(),

		}