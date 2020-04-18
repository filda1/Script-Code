from django import forms
from .models import Ponente

class PonenteForm(forms.ModelForm):
	class Meta:
		model = Ponente
		fields = ['nombre','apellidos','dni','email','grados','titulos','lugares_trabajo',]
		widgets = {'nombre':forms.TextInput(),'apellidos':forms.TextInput(),'dni':forms.TextInput(),'email':forms.TextInput(),
					'grados':forms.Textarea(),'titulos':forms.Textarea(),'lugares_trabajo':forms.Textarea(),}

sadas
dasdas