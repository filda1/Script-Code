from django import forms
from models import tipo_usuario

class Tipo_Usuario_Form(froms.ModelForm):
    class Meta:
        model : tipo_usuario
        fields=[
            'tipo',
        ]
