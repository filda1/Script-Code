from django import forms
from .models import Persona

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['dni','nombre','apellidos','numero_telefonico','email','direccion',]
        labels = {
            'dni':'Dni',
            'nombre':'Nombre',
            'apellidos':'Apellidos',
            'numero_telefonico':'Telefono',
            'email':'Email',
            'direccion':'Direccion',
        }

        widgets = {
            'dni':forms.TextInput(),
            'nombre':forms.TextInput(),
            'apellidos':forms.TextInput(),
            'numero_telefonico':forms.TextInput(),
            'email':forms.TextInput(),
            'direccion':forms.TextInput(),
        }
