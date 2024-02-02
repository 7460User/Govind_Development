from django.shortcuts import render
from django.views import View
from .forms import ResumeForms  
from .models import Resume


class homeView(View):
  
  def get(self,request): 
    form = ResumeForms()
    candadites = Resume.objects.all()
    return render(request, 'home.html',{'candadites':candadites ,'form': form})
  
  def post(self,request):
    form = ResumeForms(request.POST,request.FILES)
    if form.is_valid():
      form.save()
      return render(request,'home.html',{'form':form})

class candidateview(View):
  def get(self,request,pk):
    candidate = Resume.objects.get(pk=pk)
    return render(request,'condidate.html',{'candidate':candidate})