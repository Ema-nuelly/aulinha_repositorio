# alunos/views.py

from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect 
from django.db import IntegrityError 

from .models import Aluno, Responsavel 
from .forms import AlunoForm, ResponsavelForm 

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

class AlunoUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Aluno
    form_class = AlunoForm
    template_name = 'alunos/aluno_form.html'
    
    def get_success_url(self):
        messages.success(self.request, f"O aluno(a) {self.object.Nome} foi atualizado(a) com sucesso!")
        return reverse_lazy('alunos:lista_alunos') 

    def form_valid(self, form):
        return super().form_valid(form)
    
    def test_func(self):
        aluno = self.get_object()
        return aluno.professor == self.request.user
    
# --------------------------
# VIEWS DE RESPONSÁVEL (Adicionadas)
# --------------------------

class ResponsavelListView(LoginRequiredMixin, ListView):
    model = Responsavel
    context_object_name = 'responsaveis'
    template_name = 'alunos/responsavel_lista.html'
    
    def get_queryset(self):
        return Responsavel.objects.filter(professor=self.request.user).order_by('Nome')

class ResponsavelCreateView(LoginRequiredMixin, CreateView):
    model = Responsavel
    form_class = ResponsavelForm
    template_name = 'alunos/responsavel_form.html'
    success_url = reverse_lazy('alunos:lista_responsaveis')

    def form_valid(self, form):
        
        form.instance.professor = self.request.user 
        messages.success(self.request, f"Responsável '{form.instance.Nome}' cadastrado com sucesso!")
        return super().form_valid(form)

class ResponsavelUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Responsavel
    form_class = ResponsavelForm
    template_name = 'alunos/responsavel_form.html'
    
    def get_success_url(self):
        messages.success(self.request, f"Responsável '{self.object.Nome}' atualizado com sucesso!")
        return reverse_lazy('alunos:lista_responsaveis')

    def test_func(self):
        responsavel = self.get_object()
        return responsavel.professor == self.request.user

class ResponsavelDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Responsavel
    success_url = reverse_lazy('alunos:lista_responsaveis')
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        nome_responsavel = self.object.Nome
        
        try:
            # Chama o método de exclusão do Django
            self.object.delete() 
            messages.warning(request, f"Responsável '{nome_responsavel}' excluído com sucesso.")
            return redirect(self.get_success_url())
            
        except IntegrityError:
            
            messages.error(
                request, 
                f"Erro ao excluir '{nome_responsavel}': Este responsável ainda está ligado a um ou mais alunos. Remova ou reassocie os alunos primeiro."
            )
            return redirect(self.get_success_url())

    def test_func(self):
        responsavel = self.get_object()
        return responsavel.professor == self.request.user
