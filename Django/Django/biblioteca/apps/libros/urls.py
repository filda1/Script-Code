from django.conf.urls import url
from .views import home,create_libro,list_libro,edit_libro,delete_libro,ListarView,CrearView,EliminarView,EditarView
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^$',login_required(ListarView.as_view()),name = "home"),
    url(r'^crear_libro/',login_required(CrearView.as_view()),name = "crear_libro"),   
    url(r'^listar_libro/',login_required(ListarView.as_view()),name = "listar_libro"),  
    url(r'^editar_libro/(?P<pk>\d+)/',login_required(EditarView.as_view()),name = "editar_libro"), 
    url(r'^delete_libro/(?P<pk>\d+)/',login_required(EliminarView.as_view()),name = "eliminar_libro"), 
]