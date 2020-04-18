from django.conf.urls import url
from .views import NuevoUsuario,userlogin
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^nuevo_usuario/',login_required(userlogin),name = "nuevo_usuario"),
]
