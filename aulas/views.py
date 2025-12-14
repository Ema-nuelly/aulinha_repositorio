# aulas/views.py

from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Aula
from .forms import AulaForm

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
        return Aula.objects.filter(alunos_participantes__in=meus_alunos).distinct().order_by('Data', 'HoraInicio')