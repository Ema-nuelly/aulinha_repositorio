# materiais/urls.py

from django.urls import path
from .views import (
    MaterialListView, MaterialCreateView, MaterialUpdateView, MaterialDeleteView,
    CategoriaListView, CategoriaCreateView, CategoriaUpdateView, CategoriaDeleteView
) 

app_name = 'materiais'

urlpatterns = [
    # URLs de Material
    path('', MaterialListView.as_view(), name='lista_materiais'),
    path('novo/', MaterialCreateView.as_view(), name='criar_material'),
    path('<int:pk>/editar/', MaterialUpdateView.as_view(), name='editar_material'),
    path('<int:pk>/deletar/', MaterialDeleteView.as_view(), name='deletar_material'),
    
    # URLs de Categoria
    path('categorias/', CategoriaListView.as_view(), name='lista_categorias'),
    path('categorias/novo/', CategoriaCreateView.as_view(), name='criar_categoria'),
    path('categorias/<int:pk>/editar/', CategoriaUpdateView.as_view(), name='editar_categoria'),
    path('categorias/<int:pk>/deletar/', CategoriaDeleteView.as_view(), name='deletar_categoria'),
]