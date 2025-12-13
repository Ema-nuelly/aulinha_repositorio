# alunos/urls.py
from django.urls import path
from .views import AlunoCreateView, AlunoListView, AlunoDeleteView

app_name = 'alunos'

urlpatterns = [
    path('', AlunoListView.as_view(), name='lista_alunos'), 
    path('adicionar/', AlunoCreateView.as_view(), name='adicionar_aluno'),
    path('deletar/<int:pk>/', AlunoDeleteView.as_view(), name='deletar_aluno'),
]