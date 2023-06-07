from django.db import models

# Create your models here.


class Pessoas(models.Model):  # herança
    # campo de caracteres -> convertido em varchar
    # nome que vai ser mostrado na tabela
    nome = models.CharField(max_length=200, verbose_name="Nome")
    idade = models.IntegerField()  # Campo de inteiros  # null True -> não obrigatorio

    def __str__(self):
        return self.nome
