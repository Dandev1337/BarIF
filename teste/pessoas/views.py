from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from pessoas.models import Pessoas
from pessoas.forms import PessoaForm

def index(request):
    dsPessoas = Pessoas.objects.all()
    return render(request, "Pessoas/index.html", {'dsPessoas'})

def add(request):
    
    if request.method == "POST":
        form = PessoaForm(request.POST, instance=Pessoas)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/pessoas/')
            
    else:
        form = PessoaForm
            
    return render(request,"pessoas/add.html", {"form" : form})

def edit(request, pessoa_id):
    pessoas = pessoas.objects.get(pk=pessoa_id)
    if request.method == "POST":
        form = PessoaForm(request.POST, instance=pessoas)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/pessoas/')
            
    else:
        form = PessoaForm(instance=Pessoas)
            
    return render(request,"pessoas/edit.html", { "form" : form, 'id' : pessoa_id})
#lista os dados do usuário e confirma se quer excluir
def remove(request, pessoa_id):
    #busca a pessoa a ser excluida
    pessoa= Pessoas.objects.get(pk=pessoa_id)
    return render(request,"pessoas/confirmremove.html", { "pessoas" : pessoa_id})

def removeFinal(request, pessoa_id):
    
    return render(request,"pessoas/confirmremove.html", { "pessoas" : pessoa_id})
