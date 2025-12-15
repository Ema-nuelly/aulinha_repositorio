# 👩‍🏫 Aulinhas da Manu: Sistema de Gestão de Aulas Particulares

Sistema web desenvolvido em **Django** para gerenciar a rotina de um professor particular, facilitando o agendamento de aulas, o registro de conteúdo e o gerenciamento de materiais didáticos.

---

## ✨ Funcionalidades Principais

* **Agenda de Aulas:** Agendamento, registro e acompanhamento de aulas por aluno.
* **Gestão de Materiais:** Upload, categorização e download de materiais didáticos (apostilas, vídeos, PDFs).
* **Gestão de Alunos:** Cadastro e manutenção de informações dos alunos.
* **Autenticação:** Sistema de login e cadastro para o professor.

---

## 🛠️ Configuração e Instalação Local

Siga estes passos para configurar e rodar o projeto na sua máquina local.

### Pré-requisitos

Certifique-se de ter o [Python 3.x](https://www.python.org/downloads/) instalado no seu sistema.

### Passo a Passo de Instalação

1. **Clonar o Repositório**
   Baixe o código-fonte para o seu computador:
   ```bash
   git clone [https://github.com/Ema-nuelly/aulinha_repositorio](https://github.com/Ema-nuelly/aulinha_repositorio)
2. **Entrar na Pasta do Projeto**
   Navegue até o diretório principal:
   ```bash
   cd aulinha_repositorio
3. **Criar e Ativar o Ambiente Virtual (venv)**
   É fundamental isolar as dependências do projeto:
   ```bash
   python -m venv venv
   
   # Ativação no Linux/macOS
   source venv/bin/activate
  
   # Ativação no Windows
   .\venv\Scripts\activate
4. **Instalar Todas as Dependências**
   Instale as bibliotecas necessárias listadas no `requirements.txt`:
   ```bash
   pip install -r requirements.txt
5. **Configurar o Banco de Dados e Criar Superusuário**
   Rode as migrações para criar as tabelas e, em seguida, crie o usuário administrador (professor):
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
6. **Iniciar o Servidor de Desenvolvimento**
   Inicie a aplicação:
   ```bash
   python manage.py runserver

O sistema estará acessível no seu navegador em: `http://127.0.0.1:8000/`
## 📂 Estrutura do Projeto
O projeto é dividido nos seguintes aplicativos (apps) principais:

* `principal`: Gerencia a autenticação de usuários (login, cadastro) e o dashboard.

* `materiais`: Lida com o CRUD de materiais didáticos e categorias.

* `aulas`: Responsável pela agenda, agendamento e registro de aulas.

* `alunos`: Lida com o CRUD de informações dos alunos.
