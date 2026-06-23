from django import forms
from .models import Resenia

class ReseniaForm(forms.ModelForm):
    class Meta:
        model = Resenia
        fields = ['comentario', 'puntuacion']