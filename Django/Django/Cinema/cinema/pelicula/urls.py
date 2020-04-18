from django.conf.urls import url
from .views import CrearCategoriaPeliculaView,ListarCategoriaPeliculaView,EliminarCategoriaPeliculaView,EditarCategoriaPeliculaView,CrearRestricciones,ListarRestricciones,EditarRestricciones,EliminarRestricciones,CrearPelicula,ListarPelicula,EditarPelicula,EliminarPelicula
from django.contrib.auth.decorators import login_required

urlpatterns = [
     url(r'^crear_categoria',login_required(CrearCategoriaPeliculaView.as_view()),name='crear_categoria'),
     url(r'^listar_categoria',login_required(ListarCategoriaPeliculaView.as_view()),name='listar_categoria'),
     url(r'^editar_categoria/(?P<pk>\d+)/$',login_required(EditarCategoriaPeliculaView.as_view()),name='editar_categoria'),
     url(r'^eliminar_categoria/(?P<pk>\d+)/$',login_required(EliminarCategoriaPeliculaView.as_view()),name='eliminar_categoria'),


      url(r'^crear_restricciones',login_required(CrearRestricciones.as_view()),name='crear_restricciones'),
      url(r'^listar_restricciones',login_required(ListarRestricciones.as_view()),name='listar_restricciones'),
      url(r'^editar_restricciones/(?P<pk>\d+)/$',login_required(EditarRestricciones.as_view()),name='editar_restricciones'),
      url(r'^eliminar_restricciones/(?P<pk>\d+)/$',login_required(EliminarRestricciones.as_view()),name='eliminar_restricciones'),

      url(r'^crear_pelicula',login_required(CrearPelicula.as_view()),name='crear_pelicula'),
      url(r'^listar_peliculas',login_required(ListarPelicula.as_view()),name='listar_peliculas'),
      url(r'^editar_pelicula/(?P<pk>\d+)/$',login_required(EditarPelicula.as_view()),name='editar_pelicula'),
      url(r'^eliminar_pelicula/(?P<pk>\d+)/$',login_required(EliminarPelicula.as_view()),name='eliminar_pelicula'),
]
