from django.conf.urls import url
from .views import ReportePersonasPDF,CrearEvento,ListarEvento,EditarEvento,EliminarEvento,CrearAsistente,EditarAsistente,ListarAsistente,EliminarAsistente,CrearSeminario,ListarSeminario,EliminarSeminario,EditarSeminario
from usuarios.views import home
from django.contrib.auth.decorators import login_required

urlpatterns =  [
	url(r'^$',login_required(home),name = "index"),
	url(r'^reporte_personas_pdf/$',login_required(ReportePersonasPDF.as_view()), name="reporte_personas_pdf"),

	url(r'^crear_asistente/',login_required(CrearAsistente.as_view()),name = "crear_asistente"),
	url(r'^listar_asistente/',login_required(ListarAsistente.as_view()),name = "listar_asistente"),
	url(r'^editar_asistente/(?P<pk>\d+)/$',login_required(EditarAsistente.as_view()),name = "editar_asistente"),
	url(r'^eliminar_asistente/(?P<pk>\d+)/$',login_required(EliminarAsistente.as_view()),name = "eliminar_asistente"),

	url(r'^crear_seminario/',login_required(CrearSeminario.as_view()),name = "crear_seminario"),
	url(r'^listar_seminario/',login_required(ListarSeminario.as_view()),name = "listar_seminario"),
	url(r'^editar_seminario/(?P<pk>\d+)/$',login_required(EditarSeminario.as_view()),name = "editar_seminario"),
	url(r'^eliminar_seminario/(?P<pk>\d+)/$',login_required(EliminarSeminario.as_view()),name = "eliminar_seminario"),
	
	url(r'^crear_evento/',login_required(CrearEvento.as_view()),name = "crear_evento"),
	url(r'^listar_evento/',login_required(ListarEvento.as_view()),name = "listar_evento"),
	url(r'^editar_evento/(?P<pk>\d+)/$',login_required(EditarEvento.as_view()),name = "editar_evento"),
	url(r'^eliminar_evento/(?P<pk>\d+)/$',login_required(EliminarEvento.as_view()),name = "eliminar_evento"),
]