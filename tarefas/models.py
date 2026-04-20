from django.db import models

# Create your models here
from django.db import models

class Produto(models.Model):

    STATUS_CHOICES = [
        ('D', 'Disponível'),
        ('I', 'Indisponível'),
    ]

    CATEGORIA_CHOICES = [
        ('BRINCO', 'Brinco'),
        ('COLAR', 'Colar'),
        ('PULSEIRA', 'Pulseira'),
        ('ANEL', 'Anel'),
    ]

    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    categoria = models.CharField(max_length=20, choices=CATEGORIA_CHOICES)
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    quantidade = models.IntegerField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
    
from usuarios.models import Usuario

class Tarefa(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()

    usuario_responsavel = models.ForeignKey(
        Usuario,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.titulo