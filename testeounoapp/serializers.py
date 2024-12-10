from rest_framework import serializers
from testeounoapp.models import Proyecto
from testeounoapp.models import Cancion
from testeounoapp.models import Grupo




class serializersProyecto(serializers.ModelSerializer):
    class Meta:
        model = Proyecto
        fields = '__all__'




class serializersCancion(serializers.ModelSerializer):
    class Meta:
        model = Cancion
        fields = '__all__'
        


class serializersGrupo(serializers.ModelSerializer):
    class Meta:
        model = Grupo
        fields = '__all__'
        