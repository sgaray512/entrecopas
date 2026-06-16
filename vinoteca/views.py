from django.shortcuts import render
from .models import Vino


def home(request):

    vinos = Vino.objects.all()

    return render(
        request,
        'vinoteca/home.html',
        {
            'vinos': vinos
        }
    )
