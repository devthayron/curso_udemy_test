from django.contrib import admin
from .models import Produto, Cliente  # Importa os modelos Produto e Cliente

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque')  # Define os campos exibidos na lista do admin

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')  # Exibe nome, sobrenome e email do cliente no admin

# Registra os modelos criados no models.py no Django Admin para que possam ser gerenciados na interface administrativa
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Cliente, ClienteAdmin)
