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
        ('f',u'Femea'),
        ('m','Macho'),
    )

    nome = models.CharField(max_length=50,null=False)
    idade = models.IntegerField()
    cor = models.CharField(max_length=20,choices=CORES)
    castrado = models.BooleanField()
    sexo = models.CharField(max_length=1,choices=SEXO)
    raca = models.ForeignKey('core.Raca',verbose_name=u'raça')
    especie = models.ForeignKey('core.Especie',verbose_name=u'espécie')

    def __str__(self):
        return self.nome


class Especie(models.Model):

    PORTE = (
        ('PQ','PEQUENO'),
        ('MD','MEDIO'),
        ('GR','GRANDE'),
    )
    nome_especie = models.CharField(max_length=50)
    caracteristica = models.CharField(max_length=50,null=True)
    porte = models.CharField(max_length=50)

    def __str__(self):
        return self.nome_especie.upper()


class Raca(models.Model):

    nome = models.CharField(max_length=25)

    def __str__(self):
        return self.nome