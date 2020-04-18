from django import forms
from .models import Ponente

class PonenteForm(forms.ModelForm):
    class Meta:
        model = Ponente
        fields=[
            'nombres','apellidos','titulo','grado','lugar_trabajo',
        ]
        
        labels={
            'nombres':'Nombres',
            'apellidos':'Apellidos',
            'titulo':'Titulo',
            'grado':'Grado',
            'lugar_trabajo':'LugarTrabajo',
        }
        widgets={
            'nombres':forms.TextInput(),
            'apellidos':forms.TextInput(),
            'titulo':forms.Textarea(),
            'grado':forms.Textarea(),
            'lugar_trabajo':forms.Textarea(),
        }