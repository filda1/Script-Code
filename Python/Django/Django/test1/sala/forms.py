from django import forms
from .models import Sala,Pelicula


class PeliculaForm(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = ['nombre','nombre_alterno','duracion','categoria','fecha_estreno','idioma_original',
                    'director','sinopsis',]
        labels = {'nombre':'Nombre','nombre_alterno':'Nombre Alterno','duracion':'Duracion','categoria':'Categoria','fecha_estreno':'Fecha de Estreno',
        'idioma_original':'Idioma de Origen','director':'Director','sinopsis':'Sinopsis',}

        widgets = {'nombre':forms.TextInput(),'nombre_alterno':forms.TextInput(),'duracion':forms.TextInput(),'categoria':forms.CheckboxSelectMultiple(),'fecha_estreno':forms.TextInput(),
        'idioma_original':forms.TextInput(),'director':forms.TextInput(),'sinopsis':forms.Textarea(),}
class SalaForm(forms.ModelForm):
    class Meta:
        model = Sala
        fields = ['numero','tipo_sala','pelicula','butacas','cantidad_butacas',]
        labels = {'numero':'Numero de Sala','tipo_sala':'Tipo de sala','pelicula':'Pelicula','butacas':'Butacas','cantidad_butacas':'Numero de butacas'}
        widgets = {'numero':forms.TextInput(),'tipo_sala':forms.TextInput(),'pelicula':forms.CheckboxSelectMultiple(),'butacas':forms.CheckboxSelectMultiple(),'cantidad_butacas':forms.TextInput(),}
