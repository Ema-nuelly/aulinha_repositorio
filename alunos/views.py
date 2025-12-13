# alunos/views.py

from django.views.generic import ListView, CreateView, DeleteView # Adicione DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin # Adicione UserPassesTestMixin
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Aluno
from .forms import AlunoForm

class AlunoCreateView(LoginRequiredMixin, CreateView):
    model = Aluno
    form_class = AlunoForm
    template_name = 'alunos/aluno_form.html'
    success_url = reverse_lazy('alunos:lista_alunos') 

    def form_valid(self, form):
        form.instance.professor = self.request.user
        messages.success(self.request, "Aluno(a) adicionado(a) com sucesso!")
        return super().form_valid(form)

class AlunoListView(LoginRequiredMixin, ListView):
    model = Aluno
    context_object_name = 'alunos' 
    template_name = 'alunos/aluno_lista.html'
    
    def get_queryset(self):
        return Aluno.objects.filter(professor=self.request.user).order_by('Nome')

class AlunoDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Aluno
    success_url = reverse_lazy('alunos:lista_alunos')
    
    def test_func(self):
        aluno = self.get_object()
        return aluno.professor == self.request.user

    def form_valid(self, form):
        messages.success(self.request, f"O aluno(a) {self.object.Nome} foi deletado(a) com sucesso.")
        return super().form_valid(form)

    def handle_no_permission(self):
        messages.error(self.request, "Você não tem permissão para deletar este aluno.")
        return redirect('alunos:lista_alunos')