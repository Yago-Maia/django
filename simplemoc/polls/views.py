from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'home.html')

def contato(request):
    return render(request, 'contato.html')