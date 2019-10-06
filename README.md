# SISTEMA AUTOMATIZADO WEB PARA LA INTEROPERABILIDAD ENTRE LA FUNDACIÓN CENDITEL Y EL MPPEUCT MEDIANTE UNA APLICACIÓN REST

**Caso:** Área de Desarrollo de la Fundación Centro Nacional de Desarrollo e Investigación en Tecnologías Libres

**Trabajo Especial de Grado para Optar al Título de Técnico Superior Universitario en la Especialidad de Informática**

**Autor:** Jhonathan Salas Segura

## Software Utilizado

* Python 3.5.3
* Django 1.9.5
* Django REST 3.6.3

## Software Requerido

### GNU/Linux

    # apt-get install python-pip python-virtualenv

## Instalación del Sistema

### Windows
    > git clone https://github.com/jhonssegura/django-sistema-receptor.git
    > virtualenv entorno-receptor
    > pip install -r requirements/base.txt
    > python manage.py runserver
    
### GNU/Linux

    $ git clone https://github.com/jhonssegura/django-sistema-receptor.git
    $ virtualenv -p /usr/bin/python3 entorno-receptor
    $ pip install -r requirements/base.txt
    $ python manage.py runserver

## Configuración del Sistema

Dentro del directorio **sistema_receptor** se debe abrir el archivo de nombre **settings.py** y añadir la clave generada por el **token de autenticación** del sistema emisor.

Es importante que ambos sistemas esten corriendo, esto debido a que este sistema funciona en base a la transmisión de datos del sistema emisor.
