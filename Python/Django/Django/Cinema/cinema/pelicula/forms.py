from django import forms
from .models import CategoriaPelicula,RestriccionesPelicula,Pelicula

class CategoriaPeliculaForm(forms.ModelForm):
    class Meta:
        model = CategoriaPelicula

        fields = [
            'nombre',
        ]

        labels = {
            'nombre':'Nombre de Categoria de Pelicula'
        }

        widgets = {
            'nombre':forms.TextInput()
        }

class RestriccionesPeliculaForm(forms.ModelForm):
    class Meta:
        model = RestriccionesPelicula

        fields = [
            'nombre',
            'observaciones',
        ]

        labels = {
            'nombre':'Nombre',
            'observaciones':'Observaciones',
        }

        widgets = {
            'nombre':forms.TextInput(),
            'observaciones':forms.TextInput(),
        }

class PeliculaForm(forms.ModelForm):
    class Meta:
        model = Pelicula

        fields = [
            'nombre',
            'nombre_alterno',
            'duracion',
            'director',
            'elenco',
            'grupo_produccion',
            'fecha_estreno',
            'idioma',
            'pais',
            'distribuidora',
            'descripcion',
            'restricciones_pelicula',
            'categoria_pelicula',
        ]

        labels = {
            'nombre':'Nombre',
            'nombre_alterno':'Nombre Alterno',
            'duracion':'Duracion',
            'director':'Director',
            'elenco':'Elenco',
            'grupo_produccion':'Produccion',
            'fecha_estreno':'Fecha de Estreno',
            'idioma':'Idioma',
            'pais':'Pais origen',
            'distribuidora':'Distribuidora',
            'descripcion':'Descripcion',
            'restricciones_pelicula':'Restricciones',
            'categoria_pelicula':'Categorias',
        }

        widgets = {
            'nombre': forms.TextInput(),
            'nombre_alterno': forms.TextInput(),
            'duracion': forms.TextInput(),
            'director': forms.TextInput(),
            'elenco': forms.TextInput(),
            'grupo_produccion': forms.TextInput(),
            'fecha_estreno': forms.TextInput(attrs={'placeholder':'AAAA-MM-DD'}),
            'idioma': forms.TextInput(),
            'pais': forms.TextInput(),
            'distribuidora': forms.TextInput(),
            'descripcion': forms.TextInput(),
            'restricciones_pelicula': forms.TextInput(),
            'categoria_pelicula': forms.TextInput(),
        }
