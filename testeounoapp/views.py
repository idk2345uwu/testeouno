from django.shortcuts import render

from django.shortcuts import redirect
from testeounoapp.forms import FormProyecto
from testeounoapp.models import Proyecto

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