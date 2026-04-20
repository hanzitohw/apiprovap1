from django.urls import path
from . import views

urlpatterns = [
    path('produtos/', views.lista_produtos),
    path('produtos/disponiveis/', views.produtos_disponiveis),
]
