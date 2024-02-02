from django.shortcuts import render,redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from django.http import JsonResponse
import json
# Create your views here.


@api_view()
def home(request):
    return Response({
        'status':200,
        'message':'yes!django rest framework is working!!!!',
    })

def home_page(request):
    if request.method =='POST':
        name = request.POST.get("name")
        roll = request.POST.get("roll")
        age = request.POST.get("age")
        add = request.POST.get("add")
        student = Student(name=name,roll=roll,age=age,add=add)
        # student = Student(name="John Doe", roll=1, age=20, add="Hyderabad")
        student.save()
        return redirect('/database')
    return render(request,'home.html')


def json(request):
     data = list(Student.objects.values())
     return JsonResponse(data,safe=False)



def get_page(request):
    service = Student.objects.all()
    data = {
        'service':service
    }
    return render(request,'database.html',data)


def get_data(request):
    Service = Student.objects.all()
    data = {
        'Service':Service
    }
    return render(request,'database.html',data)
 

def delete(request, id):
    stud = Student.objects.get(id=id)
    stud.delete()
    return redirect('/database')
 


def update(request, id):
    Service= Student.objects.get(id=id)

    return render(request,'update.html',{'Service':Service})


