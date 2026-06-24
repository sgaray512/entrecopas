from django import forms
from .models import Resenia, Vino, Bodega

class ReseniaForm(forms.ModelForm):
    class Meta:
        model = Resenia
        fields = ['comentario', 'puntuacion']

class VinoForm(forms.ModelForm):
    class Meta:
        model = Vino
        fields = [
            'nombre',
            'descripcion',
            'precio',
            'stock',
            'imagen',
            'bodega',
            'categoria'
        ]

class BodegaForm(forms.ModelForm):
    class Meta:
        model = Bodega
        fields = [
            'nombre',
            'provincia',
            'descripcion'
        ]