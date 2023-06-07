from django import forms
from django.forms import ModelForm
from pessoas.models import Pessoas


class PessoaForm(ModelForm):

    # utilizado pra estilizar o form que o django gera sozinho.
    nome = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    idade = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    aceite = forms.BooleanField()

    class Meta:
        model = Pessoas
        fields = "__all__"
        
    def clean_nome(self):
        print("validou")
        
        print(self.fields["nome"])
        
        return self.fields["nome"]
        
    def save (self):
        print(self.fields)
        print("_________")
        print(self.cleaned_data["nome"])
        print("veio aqui salvar")