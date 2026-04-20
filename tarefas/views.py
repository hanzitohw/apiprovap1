from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .models import Produto

def lista_produtos(request):
    produtos = list(Produto.objects.values())
    return JsonResponse(produtos, safe=False)

def produtos_disponiveis(request):
    produtos = list(Produto.objects.filter(status='D').values())
    return JsonResponse(produtos, safe=False)

def listar_tarefas(request):
    tarefas = Tarefa.objects.all()

    lista = []
    for t in tarefas:
        lista.append({
            "id": t.id,
            "titulo": t.titulo,
            "descricao": t.descricao,
            "usuario": t.usuario_responsavel.nome if t.usuario_responsavel else None
        })

    return JsonResponse(lista, safe=False)