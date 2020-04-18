from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','is_gerente',]
        labels = {'username':'Nombre de Usuario','email':'Correo electronico',
        'first_name':'Nombre','last_name':'Apellido','is_gerente':'Nivel de usuario',}
        widgets = {'username':forms.TextInput(),'email':forms.TextInput(),'first_name':forms.TextInput(),'last_name':forms.TextInput(),
        'password':forms.TextInput(),'is_gerente':forms.CheckboxInput(),}

class CajeroForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username','email','first_name','last_name',]
        labels = {'username':'Nombre de Usuario','email':'Correo electronico',
        'first_name':'Nombre','last_name':'Apellido',}
        widgets = {'username':forms.TextInput(),'email':forms.TextInput(),'first_name':forms.TextInput(),'last_name':forms.TextInput(),
        'password':forms.TextInput(),}