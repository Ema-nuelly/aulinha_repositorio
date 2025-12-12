# alunos/models.py 

from django.db import models
from django.contrib.auth.models import User 

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
    NivelEscolar = models.CharField(max_length=50)
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