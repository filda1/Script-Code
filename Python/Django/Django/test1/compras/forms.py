from django import forms
from .models import Entrada,Funcion,TipoEntrada

class TipoEntradaForm(forms.ModelForm):
    class Meta:
        model = TipoEntrada
        fields = ['tipo',]
        labels = {'tipo':'Tipo',}
        widgets = {'tipo':forms.TextInput(),}


class EntradaForm(forms.ModelForm):
    class Meta:
        model = Entrada
        fields = ['hora_compra','cantidad','precio','tipo_entrada',
        'total_pagado','sala','pelicula',]
        labels = {'hora_compra':'Hora de Compra','cantidad':'Cantidad de entradas',
                    'precio':'Precio de cada entrada','tipo_entrada':'Tipo de entrada',
                    'total_pagado':'Total dinero entregado','sala':'Sala','pelicula':'Pelicula',}
        widgets = {'hora_compra':forms.TimeInput(),'cantidad':forms.NumberInput(),'precio':forms.Select(),
                    'tipo_entrada':forms.CheckboxSelectMultiple(),'total_pagado':forms.NumberInput(),
                    'sala':forms.Select(),'pelicula':forms.Select(),}

class FuncionForm(forms.ModelForm):
    class Meta:
        model = Funcion
        fields = ['hora_funcion','pelicula','sala',]
        labels = {'hora_funcion':'Hora de la Funcion','pelicula':'Peliculas a proyectar','sala':'Sala',}
        widgets = {'hora_funcion':forms.TimeInput(),'pelicula':forms.CheckboxSelectMultiple(),'sala':forms.Select(),}
