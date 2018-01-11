from models import *
from django import forms

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class RegistroForm(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = [
            'nombres',
            'edad',
            'profesion',
            'telefono',
            'celular',
            'rol',
            'estado',
            'email',
            'password1',
        ]
        labels = {
            'nombres': 'Nombre del Representante',
            'edad': 'Edad',
            'profesion': 'Profesion',
            'telefono': 'Telefono',
            'celular': 'Celular',
        }