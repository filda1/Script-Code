from django.conf.urls import url
from .views import CrearUsuario,home
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login,logout_then_login

urlpatterns = [
	url(r'^$',login_required(home),name = "index"),
	url(r'^crear_usuario',CrearUsuario.as_view(), name="crear_usuario"),		
 	url(r'^accounts/login', login,{'template_name':'usuarios/login.html'},name='login'),
 	url(r'^logout/',logout_then_login,name='logout'),
] 
