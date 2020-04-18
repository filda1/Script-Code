from django import forms
from .models import Libro

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo','autor','descripcion','editorial','fecha_publicacion','numero_paginas',]
        labels = {
                        'titulo':'Titulo',
                        'autor':'Autor',
                        'descripcion':'Descripcion',
                        'editorial':'Editorial',
                        'fecha_publicacion':'Fecha de publicacion',
                        'numero_paginas':'Numero de pagina',
                    }

        widgets = {
                    'titulo':forms.TextInput(),
                    'autor':forms.CheckboxSelectMultiple(),
                    'descripcion':forms.Textarea(),
                    'editorial':forms.TextInput(),
                    'fecha_publicacion':forms.DateInput(),
                    'numero_paginas':forms.NumberInput(),
                }
