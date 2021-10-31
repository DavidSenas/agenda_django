from django.db import models

#C ada Classe criada Corresponde a um Campo da Aplicação da Agenda.

# Grupos Separandos por "Amigos/Trabalho/Família.

# as 3 defs que foram criadas para que na aplicação mostrasse os nomes dos contatos.

# Caso as defs não fossem criadas, as aplicações apareceriam como Objects.

class Amigos(models.Model):
    Nome = models.CharField(max_length=50, blank=True)
    Cidade = models.CharField(max_length=50, blank=True)
    Telefone = models.CharField(max_length=20, blank=True)
    Obs = models.TextField(blank=True)
    def __str__(self):
        return self.Nome

class Trabalho(models.Model):
    Nome = models.CharField(max_length=50, blank=True)
    Cidade = models.CharField(max_length=50, blank=True)
    Telefone = models.CharField(max_length=20, blank=True)
    Empresa = models.CharField(max_length=50, blank=True)
    Obs = models.TextField(blank=True)

    def __str__(self):
        return self.Nome


class Família(models.Model):
    Nome = models.CharField(max_length=50, blank=True)
    Tipo_Parentesco = models.CharField(max_length=50, blank=True)
    Telefone = models.CharField(max_length=20, blank=True)
    Obs = models.TextField(blank=True)

    def __str__(self):
        return self.Nome

