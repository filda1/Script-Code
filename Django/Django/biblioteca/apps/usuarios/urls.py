from django.conf.urls import url
from .views import CrearUsuario
from django.contrib.auth.decorators import login_required

urlpatterns = [
	
	url(r'^crear_usuario/',login_required(CrearUsuario.as_view()),name = "crear_usuario"),
]