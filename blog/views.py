from django.shortcuts import render
from django.http import HttpResponse

def home(requets):
    return HttpResponse('<h1>Homa page</h1>')