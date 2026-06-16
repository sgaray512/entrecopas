from django.db import models
from django.conf import settings
from vinoteca.models import Vino

class Pedido(models.Model):

    ESTADOS = [
        ('PENDIENTE', 'Pendiente'),
        ('CONFIRMADO', 'Confirmado'),
        ('ENTREGADO', 'Entregado'),
    ]

    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    fecha = models.DateTimeField(auto_now_add=True)

    estado = models.CharField(
        max_length=20,
        choices=ESTADOS,
        default='PENDIENTE'
    )

    def __str__(self):
        return f"Pedido #{self.id}"
    
class DetallePedido(models.Model):

    pedido = models.ForeignKey(
        Pedido,
        on_delete=models.CASCADE,
        related_name='detalles'
    )

    vino = models.ForeignKey(
        Vino,
        on_delete=models.CASCADE
    )

    cantidad = models.IntegerField()

    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.vino} x {self.cantidad}"