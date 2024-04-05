from django.shortcuts import render,redirect
from app1.models import Employee
# Create your views here.

def  Student_data(request):
    if request.method=="POST":
        name=request.POST.get('name')
        age=request.POST.get('age') 
        email=request.POST.get('email')
        contact=request.POST.get('contact')
        emp=Employee(name=name,age=age,email=email,contact=contact)
        emp.save()
        return redirect('/data')

    return render(request,'home.html')

def Socal(request):
    obj=Employee.objects.all()
    dict1={
        'obj':obj
    }
    return render(request,'data.html',dict1)


def Delete_data(request,id):
    stdata=Employee.objects.get(id=id)
    stdata.delete()
