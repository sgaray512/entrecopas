from django.shortcuts import render
from .models import Vino
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

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

class VinoListView(ListView):
    model = Vino
    template_name = 'vinoteca/vino_list.html'
    context_object_name = 'vinos'

class VinoDetailView(DetailView):
    model = Vino
    template_name = 'vinoteca/vino_detail.html'

class VinoCreateView(CreateView):
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
    template_name = 'vinoteca/vino_form.html'
    success_url = reverse_lazy('vino_list')
class VinoUpdateView(UpdateView):
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
    template_name = 'vinoteca/vino_form.html'
    success_url = reverse_lazy('vino_list')

class VinoDeleteView(DeleteView):
    model = Vino
    template_name = 'vinoteca/vino_confirm_delete.html'
    success_url = reverse_lazy('vino_list')
