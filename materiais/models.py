# materiais/models.py

from django.db import models
from django.conf import settings 

class Categoria(models.Model):
    ID_Categoria = models.AutoField(primary_key=True)
    Nome = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.Nome

class Material(models.Model):
    ID_Material = models.AutoField(primary_key=True)
    Titulo = models.CharField(max_length=150)
    Descricao = models.TextField(blank=True)
    Arquivo = models.FileField(upload_to='materiais_didaticos/') 
    
    professor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='materiais_didaticos'
    )
    
    data_upload = models.DateTimeField(auto_now_add=True)

    categoria = models.ForeignKey(
        Categoria, 
        on_delete=models.SET_NULL, # 👈 ALTERADO: Mudar para SET_NULL
        related_name='materiais_classificados',
        null=True, # 👈 NOVO: Permite valor NULL no banco de dados
        blank=True # 👈 NOVO: Permite que seja vazio no formulário
    )

    def __str__(self):
        return self.Titulo

