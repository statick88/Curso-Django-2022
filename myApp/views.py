from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Por favor dirigete a la administración del sistema")

