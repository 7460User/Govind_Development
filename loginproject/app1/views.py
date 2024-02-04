from django.shortcuts import render


# Create your views here.
def login(request):
    context={'users':{'naresh':'n123',
                        'suresh':'sh123',
                        'ramesh':'ra123'},
            'uname':request.GET.get('t1'),
            'pwd':request.GET.get('t2')},
    return render(request,"output.html",context)

def home(request):
    return render (request,"login.html")