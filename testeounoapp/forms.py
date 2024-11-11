from django import forms
from testeounoapp.models import Proyecto
from testeounoapp.models import Cancion
from testeounoapp.models import Grupo
class FormProyecto(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = '__all__'




class FormCancion(forms.ModelForm):
    class Meta:
        model = Cancion
        fields = '__all__'


class FormGrupo(forms.ModelForm):
    class Meta:
        model = Grupo
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['integrantes'].label_from_instance = lambda obj: obj.nombre

    