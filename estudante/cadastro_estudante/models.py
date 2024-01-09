from django.db import models


class Estudantes(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    curso = models.TextField(max_length=255)
    disciplina = models.TextField(max_length=255)
    ano = models.IntegerField()
