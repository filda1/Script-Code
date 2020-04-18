from django.conf.urls import include,url
from django.contrib import admin
from views import TrabajadorList,TrabajadorCreate,index,TrabajadorUpdate,TrabajadorDelete
from django.contrib.auth.decorators import login_required

urlpatterns = [    
    url(r'^crear_trabajador/',login_required(TrabajadorCreate.as_view()), name='crear'),
    url(r'^listar_trabajador/',login_required(TrabajadorList.as_view()), name='listar'),
    url(r'^editar/(?P<pk>\d+)/$',login_required(TrabajadorUpdate.as_view()),name='editar'),
    url(r'^eliminar/(?P<pk>\d+)/$',login_required(TrabajadorDelete.as_view()),name='eliminar'),
]
