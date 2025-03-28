from django.shortcuts import render, get_object_or_404
from .models import Produto

def index(request):
    produtos = Produto.objects.all()
    context = {
        'curso': 'Programação em Python Framework',
        'produtos' : produtos,
    }
    return render(request, 'index.html',context)

def contact(request):
    return render(request,'contact.html')

def produto(request,id):
    produtos = get_object_or_404(Produto,pk=id)
    context = {
        'produto' : produtos,
        
    }
    return render(request, 'produto.html', context)