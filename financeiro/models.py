# financeiro/models.py

from django.db import models
from alunos.models import Aluno 

class Pacote(models.Model):
    ID_Pacote = models.AutoField(primary_key=True)
    Nome = models.CharField(max_length=100)
    Descricao = models.TextField(blank=True)
    Valor = models.DecimalField(max_digits=10, decimal_places=2)
    QuantidadeAulas = models.IntegerField()

    def __str__(self):
        return self.Nome

class Pagamento(models.Model):
    ID_Pagamento = models.AutoField(primary_key=True)
    DataPagamento = models.DateField(auto_now_add=True)
    ValorPago = models.DecimalField(max_digits=10, decimal_places=2)
    Metodo = models.CharField(max_length=50)

    pacote = models.OneToOneField(
        Pacote, 
        on_delete=models.SET_NULL, 
        null=True, 
        related_name='pagamento_referente'
    )
    
    aluno = models.ForeignKey(
        Aluno, 
        on_delete=models.PROTECT, 
        related_name='pagamentos_realizados'
    )

    def __str__(self):
        return f"Pagamento #{self.ID_Pagamento} - {self.aluno.Nome}"