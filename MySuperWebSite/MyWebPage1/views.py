from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(reguest):
    return HttpResponse("<center><h2>Hello World from Python DJANGO!!!</h2></center>")
