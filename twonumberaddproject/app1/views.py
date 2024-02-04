from django.shortcuts import render

# Create your views here.
def calculate(request):
   n1=int(request.GET['t1'])
   n2=int(request.GET['t2'])
   b=request.GET['b1']
   
   context={'n1':n1,'n2':n2,'b':b}
   return render(request,"calc.html",context)
def homeview(request):
    return render (request,"base.html")
       