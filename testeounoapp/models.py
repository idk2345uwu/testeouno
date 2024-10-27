from django.db import models

# Create your models here.
class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    rut = models.IntegerField()
    edad = models.IntegerField()
    grupo = models.CharField(max_length=50)
    cancion = models.CharField(max_length=100)
    localidad = models.CharField(max_length=50)


class Meta:
        db_table = 'testeounoapp_proyecto' 