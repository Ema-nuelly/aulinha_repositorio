# alunos/urls.py

from django.urls import path
from .views import AlunoCreateView, AlunoListView, AlunoDeleteView, AlunoUpdateView

app_name = 'alunos'

urlpatterns = [
    path('', AlunoListView.as_view(), name='lista_alunos'), 
    path('adicionar/', AlunoCreateView.as_view(), name='adicionar_aluno'),
    path('deletar/<int:pk>/', AlunoDeleteView.as_view(), name='deletar_aluno'),
    path('editar/<int:pk>/', AlunoUpdateView.as_view(), name='editar_aluno'), 
]