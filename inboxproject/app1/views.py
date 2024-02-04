from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,"index.html")

def signin(request):
    request.session.__setitem__('uname',request.GET.get("t1"))
    request.session.__setitem__('password',request.GET.get("t2"))
    return render(request,"output.html")

def inbox(request):
    s1=request.session.get("uname")
    
    output=f'<h2> {s1} this is your inbox </h2>'
  
    return HttpResponse(output)

