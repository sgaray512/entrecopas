from django.urls import path

from .views import (
    home,
    VinoListView,
    VinoDetailView,
    VinoCreateView,
    VinoUpdateView,
    VinoDeleteView,
)

urlpatterns = [
    path('', home, name='home'),
    path('vinos/', VinoListView.as_view(), name='vino_list'),
    path('vinos/<int:pk>/',VinoDetailView.as_view(),name='vino_detail'),
    path('vinos/nuevo/',VinoCreateView.as_view(),name='vino_create'),
    path('vinos/<int:pk>/editar/',VinoUpdateView.as_view(),name='vino_update'),
    path('vinos/<int:pk>/eliminar/',VinoDeleteView.as_view(),name='vino_delete'),
]