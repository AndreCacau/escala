from django.contrib import messages
from django.shortcuts import render, redirect
from app1.forms import PessoaModelForm, SorteioModelForm
from random import choice
from app1.models import Sorteio, Pessoa

g_dia = 0
g_coluna = 0
g_pessoa = []
g_id = 0

# Create your views here.
def index(request):
    return render(request, 'index.html')

def pessoa(request):
    if request.method == 'POST':
        form = PessoaModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Pessoa cadastrada com sucesso!')
            form = PessoaModelForm()
        else:
            messages.error(request, 'Pessoa não cadastrada')
    else:
        form = PessoaModelForm()

    context = {
        'form': form
    }
    return render (request, 'pessoa.html', context)

def sorteio(request):
    if request.method == 'POST':
        form = SorteioModelForm(request.POST)

        if form.is_valid():
            form.save()

            global g_pessoa
            g_pessoa = (form.cleaned_data['pessoas'])
            global g_dia
            g_dia = (form.cleaned_data['dias'])
            global g_coluna
            g_coluna= (form.cleaned_data['colunas'])
            global g_id
            g_id = form.instance.pk

            messages.success(request, 'Sorteio cadastrado com sucesso!')
            form = SorteioModelForm()
            return redirect(distribuicao)
        else:
            messages.error(request, 'Sorteio não cadastrado')
    else:
        form = SorteioModelForm()

    context = {
        'form': form
    }
    return render(request, 'sorteio.html', context)

def distribuicao(request):
    global g_dia
    global g_coluna
    global g_pessoa
    global g_id

    dias = list(range(1,g_dia+1))
    sorteados = []
    j = 0
    tabela = []
    for i in range(g_dia*g_coluna):
        pessoa = (choice(g_pessoa))
        sorteados.append(pessoa)
    for dia in dias:
        dias = []
        dias.append(dia)
        grupo_pessoas = []
        i = 0
        while j < (len(sorteados)):
            grupo_pessoas.append(sorteados[j])
            i += 1
            if i == g_coluna:
                i = 0
                break
            j += 1
        dias.append(grupo_pessoas)
        tabela.append(dias)

    manter_resultado(request, g_id, tabela)
    return render(request, 'tabela.html',{'sorteados':tabela})

def manter_resultado(request, id, tabela):
    sorteio = Sorteio.objects.get(id=id)
    setattr(sorteio, 'resultado', tabela)

def historico(request):
    sorteios = Sorteio.objects.all()
    return render(request, 'historico.html', {'sorteios':sorteios})

def visualizar_sorteio(request, id):
    sorteio = Sorteio.objects.get(id=id)
    lista_pessoas = []
    lista_pessoas.append(sorteio.pessoas)
    resultado = getattr(sorteio, 'resultado')
    return render(request, 'visualizar_sorteio.html',{'sorteio':sorteio, 'lista_pessoas':lista_pessoas})

def deletar_sorteio(request, id):
    sorteio = Sorteio.objects.get(id=id)
    sorteio.delete()
    sorteios = Sorteio.objects.all()
    return render(request, 'historico.html', {'sorteios':sorteios})

def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    print(pessoas)
    return render(request, 'lista_pessoas.html', {'pessoas':pessoas})

def deletar_pessoa(request, id):
    pessoa = Pessoa.objects.get(id=id)
    pessoa.delete()
    pessoas = Pessoa.objects.all()
    return render(request, 'lista_pessoas.html', {'pessoas': pessoas})