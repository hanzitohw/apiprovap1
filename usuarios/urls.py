from django.urls import path
from . import views

urlpatterns = [
    path('usuarios/', views.listar_usuarios),
    path('usuarios/<int:id>/', views.buscar_usuario_por_id),
]