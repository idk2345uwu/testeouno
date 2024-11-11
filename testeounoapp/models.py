from django.db import models

class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    rut = models.CharField(max_length=50)
    edad = models.IntegerField()
    #grupo = models.CharField(max_length=50)#
    #cancion = models.CharField(max_length=100)#
    localidad = models.CharField(max_length=50)

    class Meta:
        db_table = 'testeounoapp_proyecto'


class Cancion(models.Model):
    nombre = models.CharField(max_length=100)
    grupooriginal = models.CharField(max_length=100)
    fechaoriginal = models.DateField()
    extras = models.BooleanField()
    tematica = models.CharField(max_length=200)
    fechasalida = models.DateField()
    duracion = models.CharField(max_length=200)
    introbreak = models.BooleanField()

    def __str__(self):
        return self.nombre


class Grupo(models.Model):
    nombre = models.CharField(max_length=100)
    integrantes = models.ManyToManyField(Proyecto, related_name='grupos')
    fecha = models.DateField()
    cancion = models.ForeignKey(Cancion, on_delete=models.SET_NULL, null=True, blank=True)
    gruponuevo = models.BooleanField()

    def __str__(self):
        return self.nombre


        



