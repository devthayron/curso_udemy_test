from django.shortcuts import render,get_object_or_404
from .models import Produto
from django.http import HttpResponse
from django.template import loader


def index(request):
    produtos = Produto.objects.all()
    context = {
        'curso' : 'Python Framework Django na Udemy com o Geek',    
        'dev' : 'Dev Thayron Higlânder',
        'produtos' : produtos ,
    }
    return render(request, 'index.html',context)

def contact(request):
    return render(request, 'contact.html')

def produto(request,id):
    #prod = Produto.objects.get(pk=id)   #Busca um produto específico pelo id  # equilave a SELECT * FROM produto WHERE id = <valor_do_id>;
    prod = get_object_or_404(Produto,pk=id) #Busca um produto específico pelo id se n escontrar levanta o erro 404 
    context = {
        'produto' : prod,
    }
    return render(request, 'produto.html',context)
 

def error404(request, exception):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8',status=404)

def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)

# DEBUG com valor `True` = modo desenvolvimento

# DEBUG com valor `False` = modo produção