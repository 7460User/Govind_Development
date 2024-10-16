from django.shortcuts import render,redirect,get_object_or_404
from .models import StudentModel
# Create your views here.
def Student_views(request):
   if request.method=="POST":
       name=request.POST.get('name')
       email=request.POST.get('email')
       mob=request.POST.get('mob')
       data_base=StudentModel(name=name,email=email,mob=mob)
       data_base.save()
   return render(request,'home.html')
#    return render(request,'data_base.html')


def Get_data(request):
    new_data=StudentModel.objects.all()
    stu_data={
        'new_data':new_data
    }
    return render(request,'data_base.html',stu_data)


def delete(request,id):
    new_data=StudentModel.objects.get(id=id)
    new_data.delete()
    return redirect('/home')
    return render(request,'data_base.html')


def update(request, id):
    # Retrieve the student object or return a 404 error if it doesn't exist
    student = get_object_or_404(StudentModel, id=id)

    if request.method == "POST":
        # Update the student fields with the data from the form
        student.name = request.POST.get('name')
        student.email = request.POST.get('email')
        student.mob = request.POST.get('mob')
        student.save()  # Save the updated student object to the database
        return redirect('/home')  # Redirect to the data listing page after updating

    # Render the update form with the existing student data
    return render(request, 'update_student.html', {'student': student})

    
    
    