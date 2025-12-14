# aulas/models.py

from django.db import models
from alunos.models import Aluno
from materiais.models import Material

class Aula(models.Model):
    ID_Aula = models.AutoField(primary_key=True)
    Data = models.DateField()
    HoraInicio = models.TimeField()
    HoraFim = models.TimeField()
    Conteudo = models.TextField(blank=True)
    
    STATUS_CHOICES = [
        ('AGENDADA', 'Agendada'),
        ('REALIZADA', 'Realizada'),
        ('CANCELADA', 'Cancelada'),
    ]
    Status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='AGENDADA',
    )

    alunos_participantes = models.ManyToManyField(
        Aluno, 
        related_name='aulas_participadas'
    )

    materiais_usados = models.ManyToManyField(
        Material, 
        related_name='aulas_que_usam',
        blank=True
    )

    def __str__(self):
        return f"Aula de {self.Data} das {self.HoraInicio.strftime('%H:%M')}"