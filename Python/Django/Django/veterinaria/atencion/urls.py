from django.conf.urls import url
from views import PersonaList,PersonaCreate,PersonaDelete,PersonaUpdate,VeterinarioList,VeterinarioCreate,VeterinarioDelete,VeterinarioUpdate

urlpatterns = [    
    url(r'^listar$',PersonaList.as_view(),name='persona_list'),
    url(r'^crear$',PersonaCreate.as_view(),name='persona_create'),
    url(r'^eliminar/(?P<pk>\d+)$',PersonaDelete.as_view(),name='persona_delete'),
    url(r'^editar/(?P<pk>\d+)$',PersonaUpdate.as_view(),name='persona_editar'),
    url(r'^listar/veterinario$',VeterinarioList.as_view(),name='veterinario_list'),
    url(r'^crear/veterinario$',VeterinarioCreate.as_view(),name='veterinario_create'),
    url(r'^eliminar/veterinario/(?P<pk>\d+)$',VeterinarioDelete.as_view(),name='veterinario_delete'),
    url(r'^editar/veterinario/(?P<pk>\d+)$',VeterinarioUpdate.as_view(),name='veterinario_editar'),
]