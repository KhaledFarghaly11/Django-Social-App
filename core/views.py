from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Welcom to Social App</h1>')
