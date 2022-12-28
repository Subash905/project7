from django.shortcuts import render

# Create your views here.
def first(requst):
    return render(requst,'first.html')
def second(requst):
    return render(requst,'second.html')