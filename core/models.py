from django.db import models
# para ver os dados do DB
# from core.models import Produto
# produto = Produto.objects.all()
# produto

# para adicionar dados  
# from core.models import Produto
# produto = Produto(nome = 'Atari',preco = 1000, estoque = 47)
# produto.save()

class Produto(models.Model):
    nome = models.CharField(max_length=50)
    preco = models.DecimalField('preço', max_digits=8, decimal_places=2)
    estoque = models.IntegerField()
    
    def __str__(self):
        return self.nome
