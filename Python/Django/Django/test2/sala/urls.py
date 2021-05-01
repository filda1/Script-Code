from django.conf.urls import url
from .views import CrearPelicula,ListarPelicula,EditarPelicula,EliminarPelicula,CrearSala,EditarSala,EliminarSala,ListarSala
from django.contrib.auth.decorators import login_required

urlpatterns = [
	url(r'^nueva_pelicula/',login_required(CrearPelicula.as_view()),name = "nueva_pelicula"),
	url(r'^listar_pelicula/',login_required(ListarPelicula.as_view()),name = "listar_pelicula"),
	url(r'^editar_pelicula/(?P<pk>\d+)/$',login_required(EditarPelicula.as_view()),name = "editar_pelicula"),
	url(r'^eliminar_pelicula/(?P<pk>\d+)/$',login_required(EliminarPelicula.as_view()),name = "eliminar_pelicula"),

#Sala
	url(r'^nueva_sala/',login_required(CrearSala.as_view()),name = "nueva_sala"),
	url(r'^listar_sala/',login_required(ListarSala.as_view()),name = "listar_sala"),
	url(r'^editar_sala/(?P<pk>\d+)/$',login_required(EditarSala.as_view()),name = "editar_sala"),
	url(r'^eliminar_sala/(?P<pk>\d+)/$',login_required(EliminarSala.as_view()),name = "eliminar_sala"),
]
