from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import StudentModel
# write a bussness requirment code

def register_page(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        pswd = request.POST.get('pswd')
        contact = request.POST.get('contact')
        location = request.POST.get('location')

        # Create a new user
        user = User.objects.create_user(username=email, password=pswd)
        student_data = StudentModel(name=name, email=email, pswd=pswd, contact=contact, location=location)
        student_data.save()

        return redirect('/login')
    return render(request, 'register.html')

def login_page(request):
    if request.method == "POST":
        
        email = request.POST.get('email')
        pswd = request.POST.get('pswd')
        user = authenticate(request, username=email, password=pswd)

        if user is not None:
            
            return render(request,'logout.html')
        else:
    
            return render(request, 'login.html', {'error': 'Invalid email or password'})
    
    return render(request, 'login.html')


def logout_page(request):
    return render(request,"logout.html")



def dashboard(request):
    return render(request,"dashboard.html") 
