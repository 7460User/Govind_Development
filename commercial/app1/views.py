from django.shortcuts import render,HttpResponse,redirect
from datetime import datetime
from app1.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        "varible":"thi is sent"
    }
    return render(request,'index.html',context)
    
# fetch data in database
def about(request):
    serData = Contact.objects.all()
    data={
        'serData':serData
    }
    return render(request,'about.html',data)


def services(request):
    return render(request,'services.html')



def contact(request):
    if request.method =='POST':
      name = request.POST.get("name")
      email = request.POST.get("email")
      phone = request.POST.get("phone")
      desc = request.POST.get("desc")
      contact = Contact(name= name,email=email,phone=phone,desc=desc,date=datetime.today())
      contact.save()
    #   return redirect('/about')

      messages.success(request,"Your message hass been send..")
    return render(request,'contact.html')  


def delete(request,id):
    con = Contact.objects.get(id=id)
    con.delete()
    messages.success(request,"Your Record Deleted Successfully..")
    return redirect('/about')

def update(request,id):
    men = Contact.objects.get(id=id)
  
  
    return render(request,'contact.html',{'men':men})


def uprec(request,id):
    x=request.POST['name']
    y=request.POST['mobile']
    z=request.POST['email']
    a=request.POST['desc']
    b=request.POST['date']
    men=Contact.objects.get(id=id)
    men.name=x
    men.email=y
    men.phone=z
    men.desc=a
    men.date=b
    men.save()
    return redirect("/about")
