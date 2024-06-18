from django.shortcuts import HttpResponse

def hello(x):
    return HttpResponse("Ala ma kota")

def byk(x):
    return HttpResponse("Elo Byku Malinowy!")