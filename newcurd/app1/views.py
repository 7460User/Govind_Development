from django.shortcuts import render, redirect
from django.contrib import messages
from .models import StudentDetails

def signup(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        pwd = request.POST.get("pwd")
        confpwd = request.POST.get("confpwd")
        
        # Check if passwords match
        if pwd != confpwd:
            messages.error(request, "Passwords do not match")
            return render(request, 'home.html')

        student = StudentDetails(name=name, email=email, pwd=pwd, confpwd=confpwd)
        student.save()
        
        messages.success(request, "Account created successfully. Please log in.")
        return render(request, 'login.html')

    return render(request, 'home.html')



def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        pwd = request.POST.get('pwd')

        students = StudentDetails.objects.filter(email=email, pwd=pwd)

        if students.exists():
            student = students.first()
            return redirect('successpage')
        else:
            messages.error(request, 'Invalid username or password. Please try again!!')

    return render(request, 'login.html')        


def success(request):
    serviceDta=StudentDetails.objects.all()
    data={
        'serviceData':serviceDta
    }
    return render(request,'successpage.html',data)