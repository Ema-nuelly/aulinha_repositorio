# materiais/views.py

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages
from .forms import MaterialForm, CategoriaForm
from .models import Material, Categoria

from .models import Material

class MaterialListView(LoginRequiredMixin, ListView):
    model = Material
    context_object_name = 'materiais'
    template_name = 'materiais/material_lista.html'
    
    def get_queryset(self):
        return Material.objects.filter(professor=self.request.user).order_by('-data_upload', 'Titulo')

class MaterialCreateView(LoginRequiredMixin, CreateView):
    model = Material
    form_class = MaterialForm 
    template_name = 'materiais/material_form.html'
    success_url = reverse_lazy('materiais:lista_materiais')

    def form_valid(self, form):
        form.instance.professor = self.request.user
        messages.success(self.request, f"Material '{form.instance.Titulo}' cadastrado com sucesso!")
        return super().form_valid(form)

class MaterialUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Material
    form_class = MaterialForm 
    template_name = 'materiais/material_form.html'
    success_url = reverse_lazy('materiais:lista_materiais')

    def form_valid(self, form):
        messages.success(self.request, f"Material '{form.instance.Titulo}' atualizado com sucesso!")
        return super().form_valid(form)

    def test_func(self):
        material = self.get_object()
        return material.professor == self.request.user

class MaterialDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Material
    template_name = 'materiais/material_confirm_delete.html'
    success_url = reverse_lazy('materiais:lista_materiais')
    context_object_name = 'material'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        titulo = self.object.Titulo  

        if self.object.Arquivo:
            self.object.Arquivo.delete(save=False)

        self.object.delete()

        messages.warning(request, f"Material '{titulo}' excluído e arquivo removido com sucesso!")
        
        return redirect(success_url)

    def test_func(self):
        material = self.get_object()
        return material.professor == self.request.user

# -----------------------------------------------------------------
# CRUD DE CATEGORIAS
# -----------------------------------------------------------------

class CategoriaListView(LoginRequiredMixin, ListView):
    model = Categoria
    context_object_name = 'categorias'
    template_name = 'materiais/categoria_lista.html'

    def get_queryset(self):
        return Categoria.objects.all().order_by('Nome')


class CategoriaCreateView(LoginRequiredMixin, CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'materiais/categoria_form.html'
    success_url = reverse_lazy('materiais:lista_categorias')

    def form_valid(self, form):
        messages.success(self.request, f"Categoria '{form.instance.Nome}' criada com sucesso!")
        return super().form_valid(form)


class CategoriaUpdateView(LoginRequiredMixin, UpdateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'materiais/categoria_form.html'
    success_url = reverse_lazy('materiais:lista_categorias')

    def form_valid(self, form):
        messages.success(self.request, f"Categoria '{form.instance.nome}' atualizada com sucesso!")
        return super().form_valid(form)


class CategoriaDeleteView(LoginRequiredMixin, DeleteView):
    model = Categoria
    template_name = 'materiais/categoria_confirm_delete.html'
    success_url = reverse_lazy('materiais:lista_categorias')
    context_object_name = 'categoria'
    
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        nome = self.object.nome
        
        try:
            self.object.delete()
            messages.warning(request, f"Categoria '{nome}' excluída com sucesso!")
        except Exception as e:
            messages.error(request, f"Erro ao excluir '{nome}': ela ainda está associada a um ou mais materiais. Altere os materiais primeiro.")
            return redirect(self.request.META.get('HTTP_REFERER', success_url))
            
        return redirect(success_url)
