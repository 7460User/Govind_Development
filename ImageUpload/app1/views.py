from django.shortcuts import render,HttpResponse,redirect
from .forms import ImageForm
from  .models import Image
# Create your views here.
def homePage(request):
  if request.method == 'POST':
    form = ImageForm(request.POST,request.FILES)
    if form.is_valid():
     form.save()
  form = ImageForm()
  img = Image.objects.all()

  return render(request,'home.html',{'img':img,'form':form})

def Student_Delete(request):
   if request.method == 'POST':
      data = Image.objects.get(id=id)
      data.delete()
   return render(request,'delete.html')
  

 

 
    
        
