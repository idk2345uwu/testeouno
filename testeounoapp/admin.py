from django.contrib import admin

from .models import Proyecto, Grupo, Cancion


class proyectoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'rut', 'edad', 'localidad']




admin.site.register(Proyecto, proyectoAdmin)
admin.site.register(Grupo)
admin.site.register(Cancion)
# Register your models here.
