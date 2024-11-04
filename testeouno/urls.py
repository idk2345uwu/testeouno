"""testeouno URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from testeounoapp.views import(inicio,agregarProyecto,listadoProyectos,eliminarProyecto,actualizarProyecto,eliminarProyecto,listadoCancion,agregarCancion,eliminarCancion,actualizarCancion,listadoGrupo,agregarGrupo)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',inicio),
    path('proyectos/', listadoProyectos),
    path('agregarProyecto/', agregarProyecto),
    path('eliminarProyecto/<int:id>', eliminarProyecto),
    path('actualizarProyecto/<int:id>', actualizarProyecto),
    path('eliminarProyecto/<int:id>/', eliminarProyecto),
    path('canciones/',listadoCancion),
    path('agregarCancion/',agregarCancion),
    path('eliminarCancion/<int:id>', eliminarCancion),
    path('actualizarCancion/<int:id>', actualizarCancion),
    path('grupos/',listadoGrupo),
    path('agregarGrupo/',agregarGrupo),
]
