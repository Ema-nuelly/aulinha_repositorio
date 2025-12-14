# aulas/urls.py

from django.urls import path
from .views import AulaCreateView, AulaListView, AulaUpdateView, AulaCancelView 

app_name = 'aulas'

urlpatterns = [
    path('', AulaListView.as_view(), name='lista_aulas'), 
    path('agendar/', AulaCreateView.as_view(), name='agendar_aula'),
    path('<int:pk>/registrar/', AulaUpdateView.as_view(), name='registrar_aula'),
    path('<int:pk>/cancelar/', AulaCancelView.as_view(), name='cancelar_aula'),
]