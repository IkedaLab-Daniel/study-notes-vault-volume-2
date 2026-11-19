from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello!!!<br><a href='/hello/ice'>ice</a>")

def ice(request):
    return HttpResponse("Hello, Ice!")

def greet(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}")