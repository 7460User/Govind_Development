from django.shortcuts import render
from app1.models import Author,Book
# Create your views here.
def home(request):
    return render(request,"index.html")

def authorAdd(request):
    fname=request.POST.get("fname")
    lname=request.POST.get("lname")
    a1=Author.object.create(first_name=fname,last_name=lname)
    a1.save()
    return render(request,"index.html",{"msg":"Author Added"})

def author_add(request):
    return render(request,"Author.html")

def book_add(request):
    return render(request,"Book.html")

def addBook(request):
    title=request.POST.get("title")
    author=request.POST.get("author")
    b=Book(title=title)
    b.save()
    a=Author.object.get(author)
    b.authors.add(a)
    return render(request,"index.html",{"msg":"Book Added"})
def view_data(request):
    return render(request,"view_data.html")
def viewdata(request):
    aid=int(request.GET.get("aid"))
    qs=Book.object.filter(authors=aid)
    l=qs.value_list()
    return render(request,"output.html",{"qs":l})
    
