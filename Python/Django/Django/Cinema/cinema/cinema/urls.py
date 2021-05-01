"""cinema URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include,url
from django.contrib import admin
from django.contrib.auth.views import login,logout_then_login
from trabajador.views import index
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',login_required(index), name='index'),
    url(r'^trabajador/',include('trabajador.urls',namespace='trabajador')),
    url(r'^pelicula/',include('pelicula.urls',namespace='pelicula')),
    url(r'^usuario/',include('users.urls',namespace='users')),
    url(r'^accounts/login/',login,{'template_name':'users/login.html'},name='login'),
    url(r'^logout/',logout_then_login, name='logout'),
]
