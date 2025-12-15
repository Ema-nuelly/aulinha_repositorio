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

class ResponsavelForm(forms.ModelForm):
    class Meta:
        model = Responsavel
        exclude = ('professor', 'ID_responsavel')
        
        widgets = {
            'Nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome completo do responsável'}),
            'CPF': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '000.000.000-00'}),
            'Email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email@contato.com'}),
            'Telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(XX) XXXXX-XXXX'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
             field.widget.attrs.update({'class': 'form-control'})
