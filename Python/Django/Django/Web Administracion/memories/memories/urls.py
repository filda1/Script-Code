"""memories URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url,include
from django.contrib import admin
from usuarios.views import home,acceder,contactanos,nosotros,registro,servicios,servicios_premium,urnas,urnas2,urnas3,urnas4,urnas5,urnas6

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',home, name = "home" ),
    #url(r'^acceder/',acceder, name = "acceder" ),
    url(r'^contactanos/',contactanos, name = "contactanos" ),
    url(r'^nosotros/',nosotros, name = "nosotros" ),
    url(r'^registro/',registro, name = "registro" ),
    #url(r'^servicios/',servicios, name = "servicios" ),
    url(r'^servicios_premium/',servicios_premium, name = "servicios_premium" ),
    url(r'^urnas/',urnas, name = "urnas" ),    
    url(r'^urnas2/',urnas2, name = "urnas2" ),    
    url(r'^urnas3/',urnas3, name = "urnas3" ),    
    url(r'^urnas4/',urnas4, name = "urnas4" ),    
    url(r'^urnas5/',urnas5, name = "urnas5" ),    
    url(r'^urnas6/',urnas6, name = "urnas6" ),
]
