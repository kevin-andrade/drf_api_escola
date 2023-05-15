from django.db import models


class Aluno(models.Model):
    nome = models.CharField(max_length=30, blank=False, null=False)
    rg = models.CharField(max_length=9, blank=False, null=False)
    cpf = models.CharField(max_length=11)
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome


class Curso(models.Model):

    NIVEL_CURSO = [
        ('B', 'Básico'),
        ('I', 'Intermediário'),
        ('A', 'Avançado'),
    ]

    codigo_curso = models.CharField(max_length=10)
    descricao = models.CharField(max_length=100)
    nivel_curso = models.CharField(choices=NIVEL_CURSO, max_length=1, blank=False, null=False)

    def __str__(self):
        return self.descricao