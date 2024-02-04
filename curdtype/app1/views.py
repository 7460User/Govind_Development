from django.shortcuts import render,redirect
from app1.models import EmpDetails
# Create your views here.


def index(request):
    if request.method == "POST":
        name = request.POST.get('name')
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip = request.POST.get('zip')
        student = EmpDetails(name=name,email=email,password=password,city=city,state=state,zip=zip)
        student.save()
        return redirect('/home')
    return render(request,'home.html')


def home(request):
    sefdata = EmpDetails.objects.all()
    data = {
        'sefdata':sefdata
    }
    return render(request,'index.html',data)

def delete(request,id):
    details = EmpDetails.objects.get(id=id)
    details.delete()
    return redirect('/home')
  