from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    print("hii")
    return HttpResponse("<h1>hello mr.govind</h1>")
