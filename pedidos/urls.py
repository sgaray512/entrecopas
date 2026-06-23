from django.urls import path
from . import views

urlpatterns = [
    path('mis-pedidos/', views.mis_pedidos, name='pedidos'),
]   