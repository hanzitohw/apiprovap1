from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .models import Usuario

def listar_usuarios(request):
    usuarios = list(Usuario.objects.values())
    return JsonResponse(usuarios, safe=False)

def buscar_usuario_por_id(request, id):
    try:
        usuario = Usuario.objects.get(id=id)
        return JsonResponse({
            "id": usuario.id,
            "nome": usuario.nome,
            "email": usuario.email,
            "ativo": usuario.ativo
        })
    except Usuario.DoesNotExist:
        return JsonResponse({"erro": "Usuário não encontrado"}, status=404)