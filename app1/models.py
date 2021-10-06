from datetime import datetime
from django.db import models
from stdimage import StdImageField

# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField('Nome', max_length=100)
    #o parametro blank=true permite que nao seja obrigatorio adicionar imagem ao cadastrar uma pessoa
    imagem = StdImageField('Foto de perfil', upload_to='perfil', variations={'thumb': (90, 90)}, blank=True)
    def __str__(self):
        return self.nome

class Sorteio(models.Model):
    dias = models.IntegerField('Dias')
    colunas = models.IntegerField('Pessoas/dia')
    pessoas = models.ManyToManyField(Pessoa)
    #auto_now_add=True nao estava funcinando, esse parametro deveria atualizar a data automaticamente
    data_hora = models.DateTimeField(default=datetime.now)#felizmente desta outra maneira funcionou
    resultado = []




