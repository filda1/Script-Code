from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistroForm(UserCreationForm):

	class Meta:
		model = User
		fields = [
			'username',
			'first_name',
			'last_name',
			'email',
		]

		labels = {
			'username': 'Nombre de usuario',
			'firts_name':'Nombres' ,
			'last_name':'Apellidos' ,
			'email':'Email' ,
		}