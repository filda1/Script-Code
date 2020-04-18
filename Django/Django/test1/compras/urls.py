from django.conf.urls import url
from .views import NuevaEntrada,ListarEntrada,EditarEntrada,EliminarEntrada
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^nueva_entrada/',login_required(NuevaEntrada.as_view()),name="nueva_entrada"),
    url(r'^listar_entrada/',login_required(ListarEntrada.as_view()),name="listar_entrada"),
    url(r'^editar_entrada/(?P<pk>\d+)/$',login_required(EditarEntrada.as_view()),name="editar_entrada"),
    url(r'^eliminar_entrada/(?P<pk>\d+)/$',login_required(EliminarEntrada.as_view()),name="eliminar_entrada"),
]
