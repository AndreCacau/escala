from django.urls import path
from app1.views import index, pessoa, sorteio, distribuicao, historico, visualizar_sorteio, deletar_sorteio, lista_pessoas, deletar_pessoa

urlpatterns = [
    path('', index),
    path('pessoa', pessoa, name='pessoa'),
    path('sorteio', sorteio, name='sorteio'),
    path('tabela', distribuicao, name='tabela'),
    path('historico', historico, name='historico'),
    path('visualizar/<int:id>/', visualizar_sorteio, name='visualizar_sorteio'),
    path('deletar/<int:id>/', deletar_sorteio, name='deletar_sorteio'),
    path('lista_pessoas', lista_pessoas, name='lista_pessoas'),
    path('deletar_pessoa/<int:id>/', deletar_pessoa, name='deletar_pessoa'),
]
