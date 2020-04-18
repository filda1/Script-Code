from django import forms 
from .models import Pelicula,Sala


class PeliculaForm(forms.ModelForm):
	class Meta:
		model = Pelicula
		fields = ['nombre','nombre_alterno','duracion','categoria','fecha_estreno','idioma_original',
					'director','sinopsis',]
		labels = {'nombre':'Nombre original','nombre_alterno':'Nombre alterno','duracion':'Duracion',
		'categoria':'Categoria','fecha_estreno':'Fecha de estreno','idioma_original':'Idioma original',
					'director':'Director','sinopsis':'Sinopsis',}			
		widgets = {'nombre':forms.TextInput(),'nombre_alterno':forms.TextInput(),'duracion':forms.TextInput(),
		'categoria':forms.CheckboxSelectMultiple(),'fecha_estreno':forms.DateInput(),
		'idioma_original':forms.TextInput(),'director':forms.TextInput(),'sinopsis':forms.Textarea(),}



class SalaForm(forms.ModelForm):
	class Meta:
		model = Sala
		fields = ['numero','tipo_sala','pelicula','butacas','cantidad_butacas',]
		labels = {'numero':'Numero de sala','tipo_sala':'Tipo de sala','pelicula':'Peliculas','butacas':'Butacas',
		'cantidad_butacas':'Cantidad total de butacas',}
		widgets = {'numero':forms.NumberInput(),'tipo_sala':forms.TextInput(),'pelicula':forms.CheckboxSelectMultiple(),
		'butacas':forms.CheckboxSelectMultiple(),'cantidad_butacas':forms.NumberInput(),}
