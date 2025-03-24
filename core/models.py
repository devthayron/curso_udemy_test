from django.db import models
#python manage.py makemigrations
#python manage.py migrate

# usando o python manage.py shell
# pode usar p terminaal interativo onde pode adicionar diretamente no BD.

# passo a passo usando o exemplo da Class Produto:

# from core.models import Produto
# produto = Produto(nome = 'Atari',preco = 1000, estoque = 47)
# produto.save()

# pegar os dados do produto:

# produto = Produto.objects.all()
# produto
# iterando:  for i in produto:   
#               print(i, end=', ')

class Produto(models.Model):
    nome = models.CharField("Nome", max_length=50)
    preco = models.DecimalField("Preço", decimal_places=2, max_digits=8) 
    estoque = models.IntegerField("Quantidade de Estoque")

    def __str__(self):
        return self.nome


class Cliente(models.Model):
    first_name = models.CharField("Primeiro nome", max_length=50)
    last_name = models.CharField("Sobrenome", max_length=50)
    email = models.EmailField("E-mail", max_length=254)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'