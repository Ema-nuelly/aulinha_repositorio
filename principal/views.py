# principal/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages 
from .forms import CustomUserCreationForm

def home(request):
    return render(request, 'principal/home.html')

# Cadastro de Usuário
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Sua conta foi criada com sucesso! Você já pode fazer login.')
            return redirect('login') 
    else:
        form = CustomUserCreationForm()
        
    return render(request, 'registration/signup.html', {'form': form})

@login_required 
def dashboard(request):
    return render(request, 'principal/dashboard.html', {})