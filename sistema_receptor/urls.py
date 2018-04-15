"""sistema_receptor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from login.views import *
from cenditel.views import ListarEvento, ListarUsuario, Index, ListarRevista, ListarCurso, ListarAnalista, ListarProyecto, ListarLibro, ListarParticipante

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', 'django.contrib.auth.views.login'),
    #url(r'^index/', index),
    url(r'^register/$', register),
    url(r'^register/success/$', register_success),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', logout_page),
    url(r'^index/', Index.as_view(), name='index'),
    url(r'^listar-eventos/', ListarEvento.as_view(), name='eventos'),
    url(r'^listar-usuarios/', ListarUsuario.as_view(), name='usuarios'),
    url(r'^listar-revistas/', ListarRevista.as_view(), name='revistas'),
    url(r'^listar-cursos/', ListarCurso.as_view(), name='cursos'),
    url(r'^listar-analistas/', ListarAnalista.as_view(), name='analistas'),
    url(r'^listar-proyectos/', ListarProyecto.as_view(), name='proyectos'),
    url(r'^listar-libros/', ListarLibro.as_view(), name='libros'),
    url(r'^listar-participantes/', ListarParticipante.as_view(), name='participantes'),
]