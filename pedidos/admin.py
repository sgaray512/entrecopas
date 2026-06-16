from django.contrib import admin
from .models import Pedido, DetallePedido

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'usuario',
        'estado',
        'fecha'
    )
    list_filter = ('estado',)
    search_fields = (
        'usuario__username',
    )

@admin.register(DetallePedido)
class DetallePedidoAdmin(admin.ModelAdmin):
    list_display = (
        'pedido',
        'vino',
        'cantidad',
        'subtotal'
    )