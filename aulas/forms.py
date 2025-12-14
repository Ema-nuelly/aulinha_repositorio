# aulas/forms.py

from django import forms
from .models import Aula 
from alunos.models import Aluno 

class AulaForm(forms.ModelForm):
    class Meta:
        model = Aula
        exclude = ('ID_Aula', 'Status', 'Conteudo') 
        
        widgets = {
            'Data': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'HoraInicio': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'HoraFim': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'alunos_participantes': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }
    def __init__(self, *args, **kwargs):
        professor = kwargs.pop('professor', None) 
        super().__init__(*args, **kwargs)

        if professor:
            self.fields['alunos_participantes'].queryset = Aluno.objects.filter(
                professor=professor,
                ativo=True
            )
            self.fields['alunos_participantes'].widget.attrs.update({'class': 'form-select'})