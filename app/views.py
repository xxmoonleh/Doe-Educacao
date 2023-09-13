from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Usuario, Doacao

def index(request):
    return render(request, "app/index.html")

def sobre(request):
    return render(request, "app/sobre.html")

def doacao(request):
    return render(request, "app/doacao.html")

def contatos(request):
    return render(request, "app/contatos.html")

from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

# View de listagem de usuários
class UsuarioListView(ListView):
    model = Usuario
    template_name = 'usuario_list.html'
    context_object_name = 'usuarios'

# View de criação de usuário
class UsuarioCreateView(CreateView):
    model = Usuario
    template_name = 'usuario_form.html'
    success_url = '/usuarios/'  # URL para redirecionar após a criação de um usuário

# View de atualização de usuário
class UsuarioUpdateView(UpdateView):
    model = Usuario
    template_name = 'usuario_form.html'
    success_url = '/usuarios/'  # URL para redirecionar após a atualização de um usuário

# View de exclusão de usuário
class UsuarioDeleteView(DeleteView):
    model = Usuario
    template_name = 'usuario_confirm_delete.html'
    success_url = '/usuarios/'  # URL para redirecionar após a exclusão de um usuário

# View de listagem de doações
class DoacaoListView(ListView):
    model = Doacao
    template_name = 'doacao_list.html'
    context_object_name = 'doacoes'

# View de criação de doação
class DoacaoCreateView(CreateView):
    model = Doacao
    template_name = 'doacao_form.html'
    success_url = '/doacoes/'  # URL para redirecionar após a criação de uma doação
