from django.urls import path
from .views import index,contact, produto

urlpatterns = [
    path('', index, name='index'),
    path('contact', contact, name='contact'),
    path('produto/<int:id>', produto, name ='produto'),     #'produto/<int: id> define uma URL (dinâmica) sendo id do tipo inteiro
]                                                           # exemplo: produto/24/
