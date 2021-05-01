from django.conf.urls import url
from .views import CrearPelicula,ListarPelicula,EditarPelicula,EliminarPelicula,CrearSala,EditarSala,ListarSala,EliminarSala

urlpatterns = [
######PELICULA##############
    url(r'^crear_pelicula/',CrearPelicula.as_view(),name = "crear_pelicula"),
    url(r'^listar_pelicula/',ListarPelicula.as_view(),name = "listar_pelicula"),
    url(r'^editar_pelicula/(?P<pk>\d+)/',EditarPelicula.as_view(),name = "editar_pelicula"),
    url(r'^eliminar_pelicula/(?P<pk>\d+)/',EliminarPelicula.as_view(),name = "eliminar_pelicula"),

##########SALA##############
    url(r'^crear_sala',CrearSala.as_view(),name = "crear_sala"),
    url(r'^listar_sala',ListarSala.as_view(),name = "listar_sala"),
    url(r'^editar_sala/(?P<pk>\d+)/$',EditarSala.as_view(),name = "editar_sala"),
    url(r'^eliminar_sala/(?P<pk>\d+)/$',EliminarSala.as_view(),name = "eliminar_sala"),
]
