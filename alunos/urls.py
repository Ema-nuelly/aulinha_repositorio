# alunos/urls.py
from django.urls import path
from .views import AlunoCreateView, AlunoListView

app_name = 'alunos'

urlpatterns = [
    path('', AlunoListView.as_view(), name='lista_alunos'), 
    path('adicionar/', AlunoCreateView.as_view(), name='adicionar_aluno'),
]