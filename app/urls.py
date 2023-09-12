from django.urls import path
from . import views

app_name = "app"

urlpatterns = [
    # path("", views.index, name="index"),
    # path("doacao", views.doacao, name="doacao"),
    # path("sobre", views.sobre, name="sobre"),
    # path("contatos", views.contatos, name="contatos"),

   # URLs para as views de Usuário
    path('usuarios/', UsuarioListView.as_view(), name='usuario_list'),
    path('usuarios/novo/', UsuarioCreateView.as_view(), name='usuario_create'),
    path('usuarios/<int:pk>/editar/', UsuarioUpdateView.as_view(), name='usuario_update'),
    path('usuarios/<int:pk>/excluir/', UsuarioDeleteView.as_view(), name='usuario_delete'),
    
    # URLs para as views de Doação
    path('doacoes/', DoacaoListView.as_view(), name='doacao_list'),
    path('doacoes/nova/', DoacaoCreateView.as_view(), name='doacao_create'),
]