from django import forms
from .models import Registro

class RegistroForm(forms.ModelForm):

    class Meta:
        model = Registro
        fields = ('nombre', 'apellido', 'correo', 'celular', 'ciudad', 'terminos', 'politica')
