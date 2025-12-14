# aulas/urls.py

from django.urls import path
from .views import AulaCreateView, AulaListView

app_name = 'aulas'

urlpatterns = [
    path('', AulaListView.as_view(), name='lista_aulas'), 
    path('agendar/', AulaCreateView.as_view(), name='agendar_aula'),
]