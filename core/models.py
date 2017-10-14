from django.db import models

# Create your models here.

class Pet(models.Model):

    CORES =(
        ('P','PRETO'),
        ('B','BRANCO'),
        ('L','LARANJA'),
        ('M','MARROM'),
        ('BI','BICOLOR'),
        ('TRI','TRICOLOR'),
    )
    SEXO = (
        ('f','Femea'),
        ('m','macho'),
    )

    nome = models.CharField(max_length=50,null=False)
    idade = models.IntegerField()
    especie = models.ForeignKey('Especie')
    cor = models.CharField(max_length=20,choices=CORES)
    raca = models.ForeignKey('Raca')
    castrado = models.BooleanField()
    sexo = models.CharField(max_length=1,choices=SEXO)


class Especie(models.Model):

    PORTE = (
        ('PQ','PEQUENO'),
        ('MD','MEDIO'),
        ('GR','GRANDE'),
    )
    nome_especie = models.CharField(max_length=50)
    caracteristica = models.CharField(max_length=50)
    porte = models.CharField(max_length=50)


class Raca(models.Model):

    nome = models.CharField(max_length=25)
