from django.shortcuts import render,redirect,HttpResponse
from .models import Student
from .forms import AddStudentForm
from django.views import View
# Create your views here.
def home(request):
    stu_data = Student.objects.all()
    return render(request,'home.html',{'studata':stu_data})


def Add_Student(request):
    if request.method == 'POST':
        fm = AddStudentForm(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            roll = fm.cleaned_data['roll']
            city= fm.cleaned_data['city']
            reg = Student(name=nm,roll=roll,city=city)

            reg.save()
            fm = AddStudentForm()
    else:
        fm = AddStudentForm()
        stud = Student.objects.all()
        return render(request, 'add-student.html',{'form':fm})
    
def post(self, request):
    fm = AddStudentForm(request.POST)
    if fm.is_valid():
        fm.save()
        return redirect('/')
    else:
        return render(request, 'add-student.html',{'form':fm,'stu':stud})


def Student_Delete(request):
    
        data = request.POST
        id = data.get('id')
        studata = Student.objects.get(id=id)
        studata.delete()
        return redirect('/')

  
       