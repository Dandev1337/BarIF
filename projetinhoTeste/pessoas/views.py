from django import template
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render  # IMPORTA
from django.template import loader
from pessoas.forms import PessoaForm  # IMPORTA
from pessoas.models import Pessoas
from django.contrib.auth.decorators import login_required

# Create your views here.

# metodo que exibe todas as pessoas cadastradas
@login_required
def index(request):  # list - read

    # # carrega o template da pasta template o arquivo index.html
    # template = loader.get_template('pessoas/index.html')

    # context = {
    #     "var1": 101
    # }

    # # renderiza pro usuario a requisição que ele pediu
    # return HttpResponse(template.render(context, request))

    # -------------------------------------
    dsPessoas = Pessoas.objects.all()  # dataset -> conjunto de dados de pessoas
    return render(request, "pessoas/index.html", {'dsPessoas': dsPessoas})


# Metodo para adicionar novas pessoas
def add(request):
    # Verifica se esta vindo dados no POST
    if request.method == 'POST':
        # recupera os dados baseado no POST
        form = PessoaForm(request.POST)
        # Valida os dados
        if form.is_valid():
            # salva os dados
            form.save()
            # redireciona o user
            return HttpResponseRedirect("/pessoa/")
    else:
        # so vou mostrar o formulario
        form = PessoaForm()

    return render(request, "pessoas/add.html", {"form": form})


def edit(request, pessoa_id):  # adicionei o parametro
    # recupera a pessoa que sera editada
    pessoa = Pessoas.objects.get(pk=pessoa_id)
    # Verifica se esta vindo dados no POST
    if request.method == 'POST':
        # recupera os dados baseado no POST
        form = PessoaForm(request.POST, instance=pessoa)
        # Valida os dados
        if form.is_valid():
            # salva os dados
            form.save()
            # redireciona o user
            return HttpResponseRedirect("/pessoa/")
    else:
        # so vou mostrar o formulario
        form = PessoaForm(instance=pessoa)

    return render(request, "pessoas/edit.html", {"form": form, 'id': pessoa_id})


def remove(request, pessoa_id):
    # busca pessoa que sera excluida
    pessoa = Pessoas.objects.get(pk=pessoa_id)
    return render(request, "pessoas/confirmRemove.html", {"pessoa": pessoa})

# exclui a pessoa apos confirmacao do usuario


def removeFinal(request, pessoa_id):
    Pessoas.objects.get(pk=pessoa_id).delete()

    return HttpResponseRedirect("/pessoa/")
