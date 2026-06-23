from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Pedido

@login_required
def mis_pedidos(request):
    pedidos = Pedido.objects.filter(usuario=request.user).order_by('-fecha')
    return render(request, 'pedidos/pedidos.html', {'pedidos': pedidos})