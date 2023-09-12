import datetime
from django.db import models
from django.utils import timezone

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    endereco = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14, unique=True)
    nascimento = models.DateField()
    cep = models.CharField(max_length=9)
    senha = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)
    estado = models.CharField(max_length=2)
    bairro = models.CharField(max_length=255)
    rua = models.CharField(max_length=255)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.nome

class Doacao(models.Model):
    id = models.AutoField(primary_key=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    forma_pagamento = models.CharField(max_length=255)

    def __str__(self):
        return f"Doação de {self.valor} para {self.usuario.nome}"
