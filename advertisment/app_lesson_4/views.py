from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse('<h2><font color="#9900FF"> Домашка по 4 занятию </font></h2>')

# Create your views here.
