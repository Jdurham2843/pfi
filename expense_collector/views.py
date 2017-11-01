from django.shortcuts import render
from django.http import HttpResponse, request

def hello(request):
    return HttpResponse('Hello world')