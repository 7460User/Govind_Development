from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from .models import EmpModels

def register_page(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        pswd = request.POST.get('pswd')
        contact = request.POST.get('contact')
        location = request.POST.get('location')

        # Check if the username (email) already exists
        if User.objects.filter(username=email).exists():
            messages.error(request, 'Email already taken. Please choose another one.')
            return render(request, 'register.html')

        try:
            # Create a new user
            user = User.objects.create_user(username=email, password=pswd)
            user.save()

            # Save additional student data
            student_data = EmpModels(name=name, email=email, pswd=pswd, contact=contact, location=location)
            student_data.save()

            messages.success(request, 'User created successfully.')
            return redirect('/login')
        except IntegrityError:
            messages.error(request, 'An error occurred during registration. Please try again.')
            return render(request, 'register.html')

    return render(request, 'register.html')

def login_page(request):
    if request.method == "POST":
        email = request.POST.get('email')
        pswd = request.POST.get('pswd')
        user = authenticate(request, username=email, password=pswd)

        if user is not None:
            login(request, user)
            return render(request, 'logout.html')
        else:
            return render(request, 'login.html', {'error': 'Invalid email or password'})

    return render(request, 'login.html')

def logout_page(request):
    return render(request, "logout.html")
