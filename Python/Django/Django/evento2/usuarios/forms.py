from django import forms 
from .models import User
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username','email','first_name','last_name','is_panelista',]
		labels = {'username':'Nombre de usuario','email':'Correo','first_name':'Nombres',
					'last_name':'Apellidos','is_panelista':'Panelista',}
		widgets = {'username':forms.TextInput(),'email':forms.TextInput(),'first_name':forms.TextInput(),
				'last_name':forms.TextInput(),'is_panelista':forms.CheckboxInput(),}