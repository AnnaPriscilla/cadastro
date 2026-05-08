from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nome

class Cadastro(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=15)
    dataDeNascimento = models.DateField()
    telefone = models.CharField(max_length=15)
    email = models.EmailField()
    senha = models.CharField(max_length=100)
    confirmarSenha = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    cidade = models.CharField(max_length=50)
    estado= models.CharField(max_length=50)
    cep = models.CharField(max_length=50)