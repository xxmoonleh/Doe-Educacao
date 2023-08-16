from django.shortcuts import render

def index(request):
    return render(request, "app/index.html")

def sobre(request):
    return render(request, "app/sobre.html")

def doacao(request):
    return render(request, "app/doacao.html")

def contatos(request):
    return render(request, "app/contatos.html")

# Create your views here.
