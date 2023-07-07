from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, World!")

"""
Just saying Hello
def index(request):
    return HttpResponse("Hello!")
"""

def brian(request):
    return HttpResponse("Hello, Brian!")

def david(request):
    return HttpResponse("Hello, David")

# My personal addition
def kin(request):
    return HttpResponse("Hello, Kin")

# Greeting anyone
def greet(request, name):
    return HttpResponse(f"Hello, {name}")