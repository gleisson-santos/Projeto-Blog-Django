from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
#Utilizando classes onde a vantagem  é que você pode reutilizar o codigo com o sistema de heranças


class PostIndex(ListView):
    pass


class PostBusca(PostIndex):
    pass


class PostCategoria(PostIndex):
    pass


class PostDetalhes(PostIndex):
    pass







# Create your views here.
