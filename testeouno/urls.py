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
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from testeounoapp import views
router = DefaultRouter()
router.register('proyectos_list', views.ProyectoViewSets)
router.register('canciones_list', views.CancionesViewSets)
router.register('grupos_list', views.GruposViewSets)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.inicio),
    path('proyectos/', views.listadoProyectos),
    path('agregarProyecto/', views.agregarProyecto),
    path('eliminarProyecto/<int:id>', views.eliminarProyecto),
    path('actualizarProyecto/<int:id>', views.actualizarProyecto),
    path('eliminarProyecto/<int:id>/', views.eliminarProyecto),
    path('canciones/', views.listadoCancion),
    path('agregarCancion/', views.agregarCancion),
    path('eliminarCancion/<int:id>', views.eliminarCancion),
    path('actualizarCancion/<int:id>', views.actualizarCancion),
    path('grupos/', views.listadoGrupo),
    path('agregarGrupo/', views.agregarGrupo, name='agregarGrupo'),
    path('actualizarGrupo/<int:id>', views.actualizarGrupo),
    path('eliminarGrupo/<int:id>/', views.eliminarGrupo),
    path('api/', include(router.urls)),
    path('proyecto_list/', views.proyecto_list),
    path('proyecto_list/<int:pk>', views.proyecto_detail),
    path('cancion_list/', views.cancion_list),
    path('cancion_list/<int:pk>', views.cancion_detail),
    path('grupo_list/', views.grupo_list),
    path('grupo_list/<int:pk>', views.grupo_detail),
]
