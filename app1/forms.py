from django import forms
from app1.models import Pessoa, Sorteio

class PessoaModelForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ['nome', 'imagem']

class SorteioModelForm(forms.ModelForm):
    class Meta:
        model = Sorteio
        fields = ['dias', 'colunas', 'pessoas']