from models import *
from django import forms


class AreaForm(forms.ModelForm):
    class Meta:
        model = Area
        fields = [
            'nombre_area',
            'descripcion',
            'ruta_imagen',
        ]

class RetoForm(forms.ModelForm):
    class Meta:
        model = Reto
        fields = [
            'nombre_reto',
            'descripcion',
            'ruta_imagen',
            'tiempo',
        ]

class EmprendimientoForm(forms.ModelForm):
    class Meta:
        model = Emprendimiento
        fields = [
            'nombre_emprendimiento',
            'descripcion',
            'numero_emprendedores',
            'numero_colaboradores',
            'portafolio',
            'clientes',
            'vinculo_parquesoft',
            'cual_vinculo',
            'medio',
            'expectativas',
            'recibir',
            'aporte',
        ]
class ProductoForm(forms.ModelForm):
    class Meta:
        model = PortafolioPS
        fields = [
            'nombre',
            'descripcion',
            'ruta_imagen',

        ]

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = [
            'nombre_tarea',
            'descripcion',
            'fechainicio',
            'fechafin',

        ]