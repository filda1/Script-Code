# -*- coding: utf-8 -*-

from django import forms

from models import Mascota

class MascotaForm(forms.ModelForm):

	class Meta:
		model=Mascota


		fields = [
			'nombre',
			'sexo',
			'edad_aproximada',
			'fecha_obtencion',
			'persona',			
		] 

		labels = {

			'nombre': 'Nombre',
			'sexo': 'Sexo',
			'edad_aproximada':'Edad Aproximada',
			'fecha_obtencion':'Fecha de obtencion',
			'persona':'Dueño',			
		}

		widgets={
			'nombre':forms.TextInput(attrs={'class':'form-control'}),
			'sexo':forms.TextInput(attrs={'class':'form-control'}),
			'edad_aproximada':forms.TextInput(attrs={'class':'form-control'}),
			'fecha_obtencion':forms.TextInput(attrs={'class':'form-control'}),
			'persona':forms.Select(attrs={'class':'form-control'}),			
		}

