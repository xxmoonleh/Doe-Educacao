from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("doacao", views.doacao, name="doacao"),
    path("sobre", views.sobre, name="sobre"),
    path("contatos", views.contatos, name="contatos"),
]