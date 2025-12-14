# materiais/forms.py

from django import forms
from .models import Material, Categoria 

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['Titulo', 'Descricao', 'Arquivo', 'categoria']
        
        widgets = {
            'Titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Livro de Cálculo I'}),
            'Descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Breve descrição do material'}),
            'Arquivo': forms.FileInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-select'}),
        }
        
    def __init__(self, *args, **kwargs):
        # Aqui você pode filtrar categorias se for necessário, 
        # mas, por enquanto, apenas chama o init da classe pai.
        super().__init__(*args, **kwargs)

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['Nome']
        
        widgets = {
            'Nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Apostila de Português, Livros de Referência'}),
        }