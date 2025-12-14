# principal/forms.py (CÓDIGO FINAL CORRIGIDO PARA BOOTSTRAP)

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

# Importa o modelo de usuário correto
User = get_user_model() 

class CustomUserCreationForm(UserCreationForm):
    # Adicionar email (opcional, mas necessário se você incluiu no Meta.fields)
    email = forms.EmailField(
        label="E-mail", 
        max_length=254, 
        required=True
    )
    
    # 🌟 O MÉTODO QUE INJETA O BOOTSTRAP
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # 1. Aplica a classe 'form-control' em todos os campos
        for field_name, field in self.fields.items():
            # Verifica se é um widget de campo de texto/seleção padrão antes de aplicar
            if isinstance(field.widget, (forms.widgets.Input, forms.widgets.Textarea, forms.widgets.Select)):
                 field.widget.attrs.update({'class': 'form-control'})

        # Opcional: Remover o help_text padrão de senhas para maior limpeza
        if 'password2' in self.fields:
            self.fields['password2'].help_text = None
    
    class Meta(UserCreationForm.Meta):
        model = User
        # Inclui os campos padrão (username, password, password2) e o email
        fields = UserCreationForm.Meta.fields + ('email',)