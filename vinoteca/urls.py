from django.urls import path

from .views import (
    home,
    VinoListView,
    VinoDetailView,
    VinoCreateView,
    VinoUpdateView,
    VinoDeleteView,
    BodegaListView,
    BodegaDetailView,
    BodegaCreateView,
    BodegaUpdateView,
    BodegaDeleteView,
    ReseniaCreateView,
)

urlpatterns = [
    path('', home, name='home'),
    path('vinos/', VinoListView.as_view(), name='vino_list'),
    path('vinos/<int:pk>/',VinoDetailView.as_view(),name='vino_detail'),
    path('vinos/nuevo/',VinoCreateView.as_view(),name='vino_create'),
    path('vinos/<int:pk>/editar/',VinoUpdateView.as_view(),name='vino_update'),
    path('vinos/<int:pk>/eliminar/',VinoDeleteView.as_view(),name='vino_delete'),
    path('bodegas/',BodegaListView.as_view(),name='bodega_list'),
    path('bodegas/<int:pk>/',BodegaDetailView.as_view(),name='bodega_detail'),
    path('bodegas/nueva/',BodegaCreateView.as_view(),name='bodega_create'),
    path('bodegas/<int:pk>/editar/',BodegaUpdateView.as_view(),name='bodega_update'),
    path('bodegas/<int:pk>/eliminar/',BodegaDeleteView.as_view(),name='bodega_delete'),
    path('vinos/<int:vino_id>/resenia/',ReseniaCreateView.as_view(),name='crear_resenia'),
]