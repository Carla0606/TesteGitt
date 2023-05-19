from django.db import models

class Teste(models.Model):
    nome = models.CharField(
        max_length=150
    )
    class Teste2 (models.Model):
        idade = models.CharField(
            max_length=100
        )
        class Teste3 (models.Models):
            idade2 = models.CharField(
                max_length=100
            )