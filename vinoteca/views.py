from django.contrib.auth.mixins import (LoginRequiredMixin, PermissionRequiredMixin)
from django.shortcuts import render
from .models import Vino
from .models import Bodega
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

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

class VinoDetailView(LoginRequiredMixin, DetailView):
    model = Vino
    template_name = 'vinoteca/vino_detail.html'

class VinoCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
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
    permission_required = 'vinoteca.add_vino'

class VinoUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
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
    permission_required = 'vinoteca.change_vino'

class VinoDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Vino
    template_name = 'vinoteca/vino_confirm_delete.html'
    success_url = reverse_lazy('vino_list')
    permission_required = 'vinoteca.delete_vino'

class BodegaListView(ListView):
    model = Bodega
    template_name = 'vinoteca/bodega_list.html'
    context_object_name = 'bodegas'

class BodegaDetailView(LoginRequiredMixin, DetailView):
    model = Bodega
    template_name = 'vinoteca/bodega_detail.html'

class BodegaCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Bodega
    fields = [
        'nombre',
        'provincia',
        'descripcion'
    ]
    template_name = 'vinoteca/bodega_form.html'
    success_url = reverse_lazy('bodega_list')
    permission_required = 'vinoteca.add_bodega'

class BodegaUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Bodega
    fields = [
        'nombre',
        'provincia',
        'descripcion'
    ]
    template_name = 'vinoteca/bodega_form.html'
    success_url = reverse_lazy('bodega_list')
    permission_required = 'vinoteca.change_bodega'

class BodegaDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Bodega
    template_name = 'vinoteca/bodega_confirm_delete.html'
    success_url = reverse_lazy('bodega_list')
    permission_required = 'vinoteca.delete_bodega'