# aulas/forms.py

from django import forms
from .models import Aula
from materiais.models import Material
from alunos.models import Aluno

class AulaForm(forms.ModelForm):
    class Meta:
        model = Aula
        exclude = ('ID_Aula', 'Status', 'Conteudo', 'materiais_usados') 
        
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

class RegistroAulaForm(forms.ModelForm):
    class Meta:
        model = Aula
        fields = (
            'Data', 
            'HoraInicio', 
            'HoraFim', 
            'alunos_participantes', 
            'Conteudo', 
            'Status',
            'materiais_usados' 
        ) 
        
        widgets = {
            'Data': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'HoraInicio': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'HoraFim': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'alunos_participantes': forms.SelectMultiple(attrs={'class': 'form-select'}),
            'Status': forms.Select(attrs={'class': 'form-select'}),
            'Conteudo': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Detalhes da atividade, observações e metas para a próxima aula.'}),
            'materiais_usados': forms.SelectMultiple(attrs={'class': 'form-select'}), 
        }
    
    def __init__(self, *args, **kwargs):
        professor = kwargs.pop('professor', None)
        super().__init__(*args, **kwargs)
        
        if professor:
            self.fields['alunos_participantes'].queryset = professor.alunos.all()
            self.fields['materiais_usados'].queryset = Material.objects.filter(professor=professor)
        elif self.instance.pk and self.instance.alunos_participantes.exists():
            professor_existente = self.instance.alunos_participantes.first().professor
            self.fields['alunos_participantes'].queryset = professor_existente.alunos.all()
            self.fields['materiais_usados'].queryset = Material.objects.filter(professor=professor_existente)
class AulaFilterForm(forms.Form):
    
    aluno = forms.ModelChoiceField(
        queryset=Aluno.objects.none(), 
        required=False,
        label='Aluno',
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    
    status = forms.ChoiceField(
        choices=[('', 'Todos')] + list(Aula.STATUS_CHOICES),
        required=False,
        label='Status',
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    
    data_inicio = forms.DateField(
        required=False,
        label='De (Data Início)',
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
    )
    
    data_fim = forms.DateField(
        required=False,
        label='Até (Data Fim)',
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
    )

    def __init__(self, *args, **kwargs):
        professor = kwargs.pop('professor', None)
        super().__init__(*args, **kwargs)
        
        if professor:
            self.fields['aluno'].queryset = Aluno.objects.filter(professor=professor, ativo=True)
            self.fields['aluno'].empty_label = "Todos os alunos"

