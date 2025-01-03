from django.contrib import admin
from django.urls import include, path
from . import views
from .views import  realizar_login, logout, add_usuario2, perfil, editar_usuario, index, excluir_projeto

urlpatterns = [
    path('', views.home, name='home'),
    path('registro/', add_usuario2, name='add_usuario2'),
    path('login/', realizar_login, name='realizar_login'),
    path("logout/", logout, name="logout"),
    path("perfil/", perfil, name="perfil"),
    path("perfil/editar/", editar_usuario, name="editar_usuario"),
    path('criar_projeto/', views.criar_projeto, name='criar_projeto'),
    path("projetos2/", index, name="index"),
    path('excluir_projeto/<str:projeto_id>/', excluir_projeto, name='excluir_projeto')
]