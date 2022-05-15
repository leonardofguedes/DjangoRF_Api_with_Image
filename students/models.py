from django.db import models
from cpf_field.models import CPFField


class Student(models.Model):
    Turmas = (
        (101, 101), (201, 201), (301, 301), (401, 401), (501, 501), (601, 601),
    )
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=35)
    cpf = CPFField('cpf')
    email = models.EmailField()
    turma = models.IntegerField(choices=Turmas, blank=False)
    foto = models.ImageField(default=None, blank=True)

    def __str__(self):
        return self.nome

