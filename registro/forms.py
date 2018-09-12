from django import forms
from .models import RegistroCodigo

class RegistroForm(forms.ModelForm):

    class Meta:
        model = RegistroCodigo
        fields = ('nombre', 'apellido', 'correo', 'celular', 'ciudad', 'terminos', 'politica')
