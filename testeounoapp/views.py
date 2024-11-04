from django.shortcuts import render

from django.shortcuts import redirect

from testeounoapp.forms import FormProyecto
from testeounoapp.models import Proyecto

from testeounoapp.forms import FormCancion
from testeounoapp.models import Cancion


from testeounoapp.forms import FormGrupo
from testeounoapp.forms import Grupo

from django.shortcuts import get_object_or_404, redirect

# Create your views here.
def inicio(request):
    return render(request, 'testeounoapp/inicio.html')
def listadoProyectos(request):
    proyectos = Proyecto.objects.all()
    data = {'proyectos' : proyectos}
    return render(request, 'testeounoapp/proyectos.html', data)
def agregarProyecto(request):
    form = FormProyecto()
    if request.method == 'POST':
        form = FormProyecto(request.POST)
        if form.is_valid():
            form.save()
        return inicio(request)
    data = {'form' : form}
    return render(request, 'testeounoapp/agregarProyecto.html', data)
def eliminarProyecto(request, id):
    proyecto = Proyecto.objects.get(id = id)
    proyecto.delete()
    return redirect('/testeouno')
def actualizarProyecto(request, id):
    proyecto = Proyecto.objects.get(id = id)
    form = FormProyecto(instance=proyecto)
    if request.method == 'POST' :
        form = FormProyecto(request.POST, instance=proyecto)
        if form.is_valid() :
            form.save()
        return inicio(request)
    data = {'form' : form}
    return render(request, 'testeounopp/agregarProyecto.html', data)
def eliminarProyecto(request, id):
    proyecto = get_object_or_404(Proyecto, id=id)
    proyecto.delete()
    return redirect('/proyectos')




def listadoCancion(request):
    canciones = Cancion.objects.all()
    data = {'canciones' : canciones}
    return render(request, 'testeounoapp/canciones.html', data)
def agregarCancion(request):
    form = FormCancion()
    if request.method == 'POST':
        form = FormCancion(request.POST)
        if form.is_valid():
            form.save()
        return inicio(request)
    data = {'form' : form}
    return render(request, 'testeounoapp/agregarCancion.html', data)


def actualizarCancion(request, id):
    cancion = Cancion.objects.get(id = id)
    form = FormCancion(instance=cancion)
    if request.method == 'POST' :
        form = FormCancion(request.POST, instance=cancion)
        if form.is_valid() :
            form.save()
        return inicio(request)
    data = {'form' : form}
    return render(request, 'testeounopp/agregarCancion.html', data)
def eliminarCancion(request, id):
    cancion = get_object_or_404(Cancion, id=id)
    cancion.delete()
    return redirect('/canciones')










def listadoGrupo(request):
    grupos = Grupo.objects.all()
    data = {'grupos' : grupos}
    return render(request, 'testeounoapp/grupos.html', data)
def agregarGrupo(request):
    form = FormGrupo()
    if request.method == 'POST':
        form = FormGrupo(request.POST)
        if form.is_valid():
            form.save()
        return inicio(request)
    data = {'form' : form}
    return render(request, 'testeounoapp/agregarGrupo.html', data)


def actualizarGrupo(request, id):
    grupo = Grupo.objects.get(id = id)
    form = FormGrupo(instance=grupo)
    if request.method == 'POST' :
        form = FormGrupo(request.POST, instance=grupo)
        if form.is_valid() :
            form.save()
        return inicio(request)
    data = {'form' : form}
    return render(request, 'testeounopp/agregarGrupo.html', data)
def eliminarGrupo(request, id):
    grupo = get_object_or_404(Grupo, id=id)
    grupo.delete()
    return redirect('/grupos')