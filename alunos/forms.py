# alunos/forms.py

from django import forms
from .models import Aluno, Responsavel 

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        exclude = ('professor', 'ID_Aluno', 'ObservacoesProgresso', 'ativo') 
        
        widgets = {
            'Nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome completo do aluno'}),
            'DataNascimento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'responsavel': forms.Select(attrs={'class': 'form-select'}), 
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['NivelEscolar'].widget.attrs.update({'class': 'form-select'})