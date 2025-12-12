# alunos/models.py 

from django.db import models
from django.contrib.auth.models import User 

NIVEL_ESCOLAR_CHOICES = [
    ('1_ANO_FUNDAMENTAL', '1º ano do Ensino Fundamental'),
    ('2_ANO_FUNDAMENTAL', '2º ano do Ensino Fundamental'),
    ('3_ANO_FUNDAMENTAL', '3º ano do Ensino Fundamental'),
    ('4_ANO_FUNDAMENTAL', '4º ano do Ensino Fundamental'),
    ('5_ANO_FUNDAMENTAL', '5º ano do Ensino Fundamental'),    
    ('6_ANO_FUNDAMENTAL', '6º ano do Ensino Fundamental'),
    ('7_ANO_FUNDAMENTAL', '7º ano do Ensino Fundamental'),
    ('8_ANO_FUNDAMENTAL', '8º ano do Ensino Fundamental'),
    ('9_ANO_FUNDAMENTAL', '9º ano do Ensino Fundamental'),
    ('ENSINO_MEDIO', 'Ensino Médio'),
    ('SUPERIOR', 'Ensino Superior'),
    ('EJA', 'Educação de Jovens e Adultos (EJA)'),
    ('OUTRO', 'Outro'),
]
class Responsavel(models.Model):
    ID_Responsavel = models.AutoField(primary_key=True)
    Nome = models.CharField(max_length=100)
    CPF = models.CharField(max_length=14, unique=True)
    Email = models.EmailField(max_length=100, unique=True, blank=True, null=True)
    Telefone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.Nome

class Aluno(models.Model):
    ID_Aluno = models.AutoField(primary_key=True)
    
    professor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='alunos', null=True) 
    
    Nome = models.CharField(max_length=100)
    DataNascimento = models.DateField()
    NivelEscolar = models.CharField(
        max_length=50, 
        choices=NIVEL_ESCOLAR_CHOICES, 
        default='OUTRO', 
        blank=False, 
        null=False, 
        db_index=True)
    ObservacoesProgresso = models.TextField(blank=True)
    
    responsavel = models.ForeignKey(
        Responsavel, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name='alunos_associados'
    )

    def __str__(self):
        return self.Nome

