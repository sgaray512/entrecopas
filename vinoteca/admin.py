from django.contrib import admin
from .models import Bodega, Categoria, Vino, Resenia

@admin.register(Bodega)
class BodegaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'provincia')
    search_fields = ('nombre',)
    ordering = ('nombre',)

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

@admin.register(Vino)
class VinoAdmin(admin.ModelAdmin):
    list_display = (
        'nombre',
        'precio',
        'stock',
        'bodega',
        'categoria'
    )
    search_fields = (
        'nombre',
        'bodega__nombre'
    )
    list_filter = (
        'categoria',
        'bodega'
    )
    ordering = ('nombre',)

@admin.register(Resenia)
class ReseniaAdmin(admin.ModelAdmin):
    list_display = (
        'usuario',
        'vino',
        'puntuacion',
        'fecha'
    )
    list_filter = ('puntuacion',)
