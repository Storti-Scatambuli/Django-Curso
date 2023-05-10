from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'recipes/home.html', context={'name': 'VÔ ZIRALDO'})


def contato(request):
    return HttpResponse("CONTATO")


def quemsomos(request):
    return HttpResponse("QUEM SOMOS")
