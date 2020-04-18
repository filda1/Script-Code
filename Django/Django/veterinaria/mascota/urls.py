from django.conf.urls import url
from mascota.views import MascotaList,MascotaCreate,MascotaUpdate,MascotaDelete

urlpatterns = [    
    url(r'^listar$',MascotaList.as_view(),name='home_mascota'),
    url(r'^nuevo$',MascotaCreate.as_view(),name='crear_mascota'),
    url(r'^editar/(?P<pk>\d+)/$',MascotaUpdate.as_view(),name='editar_mascota'),
    url(r'^eliminar/(?P<pk>\d+)/$',MascotaDelete.as_view(),name='eliminar_mascota'),
]