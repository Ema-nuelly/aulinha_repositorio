# aulas/views.py

from django.views.generic import CreateView, ListView, UpdateView, RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect
from .models import Aula
from .forms import AulaForm, RegistroAulaForm, AulaFilterForm
from django.shortcuts import get_object_or_404

class AulaCreateView(LoginRequiredMixin, CreateView):
    model = Aula
    form_class = AulaForm
    template_name = 'aulas/aula_form.html'
    success_url = reverse_lazy('aulas:lista_aulas') 

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['professor'] = self.request.user 
        return kwargs

    def form_valid(self, form):
        form.instance.Status = 'AGENDADA' 
        messages.success(self.request, "Aula agendada com sucesso!")
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('aulas:lista_aulas')
    
    def form_invalid(self, form):
        print("--- FORMULÁRIO INVÁLIDO ---")
        print("Erros Gerais:", form.errors)
        
        for field, errors in form.errors.items():
            print(f"Campo {field}: {errors}")
            
        return super().form_invalid(form)

class AulaListView(LoginRequiredMixin, ListView):
    model = Aula
    context_object_name = 'aulas'
    template_name = 'aulas/aula_lista.html'
    
    def get_queryset(self):
        meus_alunos = self.request.user.alunos.all()
        queryset = Aula.objects.filter(alunos_participantes__in=meus_alunos).distinct().order_by('Data', 'HoraInicio')
        
        form = AulaFilterForm(self.request.GET, professor=self.request.user)
        
        if form.is_valid():
            aluno = form.cleaned_data.get('aluno')
            status = form.cleaned_data.get('status')
            data_inicio = form.cleaned_data.get('data_inicio')
            data_fim = form.cleaned_data.get('data_fim')
            
            # Aplicar filtro por Aluno
            if aluno:
                # Filtra aulas que este aluno está participando
                queryset = queryset.filter(alunos_participantes=aluno)
                
            # Aplicar filtro por Status
            if status:
                queryset = queryset.filter(Status=status)
                
            # Aplicar filtro por Período de Data
            if data_inicio:
                queryset = queryset.filter(Data__gte=data_inicio) # Data maior ou igual
                
            if data_fim:
                queryset = queryset.filter(Data__lte=data_fim) # Data menor ou igual
        
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Passa o formulário preenchido (com os valores do GET request) para o template
        context['form_filtro'] = AulaFilterForm(self.request.GET, professor=self.request.user)
        
        return context
class AulaUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

    model = Aula
    form_class = RegistroAulaForm 
    template_name = 'aulas/aula_form.html' 
    
    def get_success_url(self):
        return reverse_lazy('aulas:lista_aulas')
        
    def form_valid(self, form):
        messages.success(self.request, f"Aula de {self.object.Data} atualizada com sucesso!")
        
        return super().form_valid(form)
        
    def test_func(self):
        aula = self.get_object()
        meus_alunos = self.request.user.alunos.all()
        tem_meu_aluno = aula.alunos_participantes.filter(pk__in=meus_alunos.values_list('pk', flat=True)).exists()
        return tem_meu_aluno
        
    def handle_no_permission(self):
        messages.error(self.request, "Você não tem permissão para editar esta aula.")
        return redirect('aulas:lista_aulas')

class AulaCancelView(LoginRequiredMixin, UserPassesTestMixin, RedirectView):
    
    def get_redirect_url(self, *args, **kwargs):
        return reverse_lazy('aulas:lista_aulas')

    def test_func(self):
        from django.shortcuts import get_object_or_404 
        aula = get_object_or_404(Aula, pk=self.kwargs['pk'])
        meus_alunos = self.request.user.alunos.all()
        return aula.alunos_participantes.filter(pk__in=meus_alunos.values_list('pk', flat=True)).exists()
        
    def get(self, request, *args, **kwargs):
        if self.test_func():
            aula = get_object_or_404(Aula, pk=kwargs['pk'])
            
            if aula.Status == 'AGENDADA':
                aula.Status = 'CANCELADA'
                aula.save()
            else:
                messages.error(request, f"Não é possível cancelar uma aula que está '{aula.get_Status_display()}'.")
        
        return super().get(request, *args, **kwargs)

    def handle_no_permission(self):
        messages.error(self.request, "Você não tem permissão para cancelar esta aula.")
        return redirect('aulas:lista_aulas')

