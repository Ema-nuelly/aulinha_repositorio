# alunos/urls.py

from django.urls import path
from .views import (
    AlunoCreateView, AlunoListView, AlunoDeleteView, AlunoUpdateView,
    ResponsavelListView, ResponsavelCreateView, 
    ResponsavelUpdateView, ResponsavelDeleteView
)

app_name = 'alunos'

urlpatterns = [
    # ROTAS PARA ALUNOS 
    path('', AlunoListView.as_view(), name='lista_alunos'), 
    path('adicionar/', AlunoCreateView.as_view(), name='adicionar_aluno'),
    path('deletar/<int:pk>/', AlunoDeleteView.as_view(), name='deletar_aluno'),
    path('editar/<int:pk>/', AlunoUpdateView.as_view(), name='editar_aluno'), 
    
    # ROTAS PARA RESPONSÁVEIS
    path('responsaveis/', ResponsavelListView.as_view(), name='lista_responsaveis'),
    path('responsaveis/adicionar/', ResponsavelCreateView.as_view(), name='adicionar_responsavel'),
    path('responsaveis/editar/<int:pk>/', ResponsavelUpdateView.as_view(), name='editar_responsavel'),
    path('responsaveis/deletar/<int:pk>/', ResponsavelDeleteView.as_view(), name='deletar_responsavel'),
]