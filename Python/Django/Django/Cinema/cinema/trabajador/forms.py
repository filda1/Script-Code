from django import forms
from models import Trabajador

class TrabajadorForm(forms.ModelForm):
    class Meta:
        model = Trabajador

        fields = [
            'nombre',
            'apellido',
            'username',
            'area',
            'dni',
            'email',
            'tipo_usuario',
            'sexo',
        ]

        labels={
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'username': 'Nombre de usuario',
            'area': 'Area',
            'dni':'DNI',
            'email':'Correo Electronico',
            'sexo':'Sexo',
            'tipo_usuario':'Tipo de Usuario',
        }

        widgets = {

            'nombre':forms.TextInput(attrs={'class':'w3-input w3-border','type':'text','placeholder':'Nombre','name':'nombre',}),
            'apellido':forms.TextInput(attrs={'class':'w3-input w3-border','type':'text','placeholder':'Apellido','name':'apellido',}),
            'username':forms.TextInput(attrs={'class':'w3-input w3-border','type':'text','placeholder':'Username','name':'username',}),
            'area':forms.TextInput(attrs={'class':'w3-input w3-border','type':'text','placeholder':'Area','name':'area',}),
            'dni':forms.TextInput(attrs={'class':'w3-input w3-border','type':'text','placeholder':'Dni','name':'dni',}),
            'email':forms.TextInput(attrs={'class':'w3-input w3-border','type':'text','placeholder':'Email','name':'email',}),
            'tipo_usuario':forms.TextInput(attrs={'class':'w3-input w3-border','type':'text','placeholder':'Tipo Usuario','name':'tipo',}),
            'sexo':forms.TextInput(attrs={'class':'w3-input w3-border','type':'text','placeholder':'Sexo','name':'sexo',}),
        }
