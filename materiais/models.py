# materiais/models.py

from django.db import models

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
    
    categoria = models.ForeignKey(
        Categoria, 
        on_delete=models.PROTECT, 
        related_name='materiais_classificados'
    )

    def __str__(self):
        return self.Titulo