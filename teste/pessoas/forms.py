from django.forms import ModelForm
from pessoas.models import Pessoas

class PessoaForm(ModelForm):
    class Meta:
        model = Pessoas
        fields = '__all__'