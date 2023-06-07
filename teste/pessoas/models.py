from django.db import models

class Pessoas(models.Model):
    nome = models.CharField(max_length=200)
    idade = models.IntegerField()
