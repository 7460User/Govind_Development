from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def show1(request):
    return HttpResponse("<h1>This is show1</h1>")

def show2(request):
    return HttpResponse("<h1>This is show2</h1>")


def show3(request):
    return HttpResponse("<h1>This is show3</h1>")
   
