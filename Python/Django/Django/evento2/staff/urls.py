from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from .views import CrearPonente,EditarPonente,EliminarPonente,ListarPonente


urlpatterns =  [
url(r'^crear_ponente/',login_required(CrearPonente.as_view()),name="crear_ponente"),
	url(r'^listar_ponente/',login_required(ListarPonente.as_view()),name="listar_ponente"),
	url(r'^editar_ponente/(?P<pk>\d+)/$',login_required(EditarPonente.as_view()),name="editar_ponente"),
	url(r'^eliminar_ponente/(?P<pk>\d+)/$',login_required(EliminarPonente.as_view()),name="eliminar_ponente"),

	
]