from django.shortcuts import render
from django.views.generic import TemplateView
from sistema_receptor.settings import API_URL, API_TOKEN
import requests

class Index(TemplateView):
    template_name = 'index.html'


class ListarUsuario(TemplateView):
    template_name = "listar-usuarios.html"

    def get_context_data(self,**kwargs):
        header = {'Authorization':'Token '+API_TOKEN}
        r = requests.get(API_URL+'users', headers=header)
        data = r.json()
        kwargs['usuarios'] = data
        return super(ListarUsuario,self).get_context_data(**kwargs)


class ListarEvento(TemplateView):
    template_name = "listar-eventos.html"

    def get_context_data(self,**kwargs):
        header = {'Authorization':'Token '+API_TOKEN}
        r = requests.get(API_URL+'eventos', headers=header)
        data = r.json()
        kwargs['eventos'] = data
        return super(ListarEvento,self).get_context_data(**kwargs)


class ListarRevista(TemplateView):
    template_name = "listar-revistas.html"

    def get_context_data(self,**kwargs):
        header = {'Authorization':'Token '+API_TOKEN}
        r = requests.get(API_URL+'revistas', headers=header)
        data = r.json()
        kwargs['revistas'] = data
        return super(ListarRevista,self).get_context_data(**kwargs)


class ListarCurso(TemplateView):
    template_name = "listar-cursos.html"

    def get_context_data(self,**kwargs):
        header = {'Authorization':'Token '+API_TOKEN}
        r = requests.get(API_URL+'cursos', headers=header)
        data = r.json()
        kwargs['cursos'] = data
        return super(ListarCurso,self).get_context_data(**kwargs)


class ListarProyecto(TemplateView):
    template_name = "listar-proyectos.html"

    def get_context_data(self,**kwargs):
        header = {'Authorization':'Token '+API_TOKEN}
        r = requests.get(API_URL+'proyectos', headers=header)
        data = r.json()
        kwargs['proyectos'] = data
        return super(ListarProyecto,self).get_context_data(**kwargs)


class ListarLibro(TemplateView):
    template_name = "listar-libros.html"

    def get_context_data(self,**kwargs):
        header = {'Authorization':'Token '+API_TOKEN}
        r = requests.get(API_URL+'libros', headers=header)
        data = r.json()
        kwargs['libros'] = data
        return super(ListarLibro,self).get_context_data(**kwargs)


class ListarParticipante(TemplateView):
    template_name = "listar-participantes.html"

    def get_context_data(self,**kwargs):
        header = {'Authorization':'Token '+API_TOKEN}
        r = requests.get(API_URL+'participantes', headers=header)
        data = r.json()
        kwargs['participantes'] = data
        return super(ListarParticipante,self).get_context_data(**kwargs)


class ListarInvestigador(TemplateView):
    template_name = "listar-investigadores.html"

    def get_context_data(self,**kwargs):
        header = {'Authorization':'Token '+API_TOKEN}
        r = requests.get(API_URL+'investigadores', headers=header)
        data = r.json()
        kwargs['investigadores'] = data
        return super(ListarInvestigador,self).get_context_data(**kwargs)
