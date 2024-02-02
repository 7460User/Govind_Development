from django.shortcuts import render
from app1.models import *



# Create your views here.

   

def show_home_page(request):
    cats = Category.objects.all()
    images = Image.objects.all()
    data = {'images':images,'cats':cats}
    return render(request,"home.html",data)    



    
def show_category_page(request,cid):
    print(cid)
    cats = Category.objects.all()
    category=Category.objects.get(pk=cid)

    images = Image.objects.filter(cat=category)
    data = {'images':images,'cats':cats}
    return render(request,"home.html",data) 

 
