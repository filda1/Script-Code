from django.conf.urls import url
from .views import home, UserCreate
from django.contrib.auth.decorators import login_required

urlpatterns =  [
	url(r'^$',login_required(home),name = "index"),
	url(r'^nuevo_usuario/',UserCreate.as_view(),name = "crear_usuario"),
]