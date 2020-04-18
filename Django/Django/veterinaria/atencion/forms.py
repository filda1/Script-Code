# -*- coding: utf-8 -*-

from django import forms

from models import Persona,Veterinario

class PersonaForm(forms.ModelForm):

	class Meta:
		model=Persona

		fields = [
			'dni',
			'nombre',
			'apellidos',
			'edad',
			'telefono',
			'email',
			'domicilio',			
		] 

		labels = {

			'dni':'DNI',
			'nombre':'Nombre' ,
			'apellidos':'Apellidos' ,
			'edad':'Edad' ,
			'telefono':'Telefono' ,
			'email':'Email' ,
			'domicilio':'Direccion' ,			
		}

		widgets={
			'dni':forms.TextInput(attrs={'class':'form-control'}),
			'nombre':forms.TextInput(attrs={'class':'form-control'}),
			'apellidos':forms.TextInput(attrs={'class':'form-control'}),
			'edad':forms.TextInput(attrs={'class':'form-control'}),
			'telefono':forms.TextInput(attrs={'class':'form-control'}),
			'email':forms.TextInput(attrs={'class':'form-control'}),			
			'domicilio':forms.TextInput(attrs={'class':'form-control'}),			
		}

class VeterinarioForm(forms.ModelForm):
	class Meta:
		model=Veterinario

		fields = [
			'codigomedico',
			'dni',
			'nombre',
			'apellidos',
			'fecha_nacimiento',
			'telefono',
			'email',
			'domicilio',
			'fecha_contratacion',
			'horario',			
		] 

		labels = {

			'codigomedico':'Codigo Medico',
			'dni':'DNI',
			'nombre':'Nombre' ,
			'apellidos':'Apellidos' ,
			'fecha_nacimiento':'Fecha de Nacimiento' ,
			'telefono':'Telefono' ,
			'email':'Email' ,
			'domicilio':'Direccion' ,
			'fecha_contratacion':'Contratacion',
			'horario':'Horario',
		}

		widgets={
			'codigomedico':forms.TextInput(attrs={'class':'form-control'}),
			'dni':forms.TextInput(attrs={'class':'form-control'}),
			'nombre':forms.TextInput(attrs={'class':'form-control'}),
			'apellidos':forms.TextInput(attrs={'class':'form-control'}),
			'fecha_nacimiento':forms.TextInput(attrs={'class':'form-control'}),
			'telefono':forms.TextInput(attrs={'class':'form-control'}),
			'email':forms.TextInput(attrs={'class':'form-control'}),			
			'domicilio':forms.TextInput(attrs={'class':'form-control'}),
			'fecha_contratacion':forms.TextInput(attrs={'class':'form-control'}),
			'horario':forms.TextInput(attrs={'class':'form-control'}),			
		}