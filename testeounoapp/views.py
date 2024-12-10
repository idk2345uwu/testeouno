from django.shortcuts import render

from django.shortcuts import redirect

from testeounoapp.forms import FormProyecto
from testeounoapp.models import Proyecto

from testeounoapp.forms import FormCancion
from testeounoapp.models import Cancion


from testeounoapp.forms import FormGrupo
from testeounoapp.forms import Grupo

from django.shortcuts import get_object_or_404, redirect



from testeounoapp.serializers import serializersProyecto
from testeounoapp.serializers import serializersCancion
from testeounoapp.serializers import serializersGrupo
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

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
    grupos = Grupo.objects.prefetch_related('integrantes').all()
    return render(request, 'testeounoapp/grupos.html', {'grupos': grupos})
def agregarGrupo(request):
    form = FormGrupo()
    if request.method == 'POST':
        form = FormGrupo(request.POST)
        if form.is_valid():
            grupo = form.save(commit=False)
            grupo.save()
            form.save_m2m()
            return inicio(request)
    data = {'form': form}
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






@api_view(['GET', 'POST'])
def proyecto_list(request):
    if request.method=='GET':
        proyectos = Proyecto.objects.all()
        serializer = serializersProyecto(proyectos, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = serializersProyecto(data = request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
def proyecto_detail(request, pk):
    try:
        proyecto = Proyecto.objects.get(pk=pk)
    except Proyecto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = serializersProyecto(proyecto)
        return Response(serializer.data)
    

    if request.method == 'PUT':
        serializer = serializersProyecto(proyecto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        proyecto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)






@api_view(['GET', 'POST'])
def cancion_list(request):
    if request.method == 'GET':
        canciones = Cancion.objects.all()
        serializer = serializersCancion(canciones, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = serializersCancion(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def cancion_detail(request, pk):
    try:
        cancion = Cancion.objects.get(pk=pk)
    except Cancion.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = serializersCancion(cancion)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = serializersCancion(cancion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        cancion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def grupo_list(request):
    if request.method == 'GET':
        grupos = Grupo.objects.all()
        serializer = serializersGrupo(grupos, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = serializersGrupo(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def grupo_detail(request, pk):
    try:
        grupo = Grupo.objects.get(pk=pk)
    except Grupo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = serializersGrupo(grupo)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = serializersGrupo(grupo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        grupo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)