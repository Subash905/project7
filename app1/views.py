from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def string1(request):
    return HttpResponse('<h1>This is app1 string1 views</h1>')
def string2(request):
    return HttpResponse('<h1>This is app1 string2 views</h1>')