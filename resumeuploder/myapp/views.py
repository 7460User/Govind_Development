from django.shortcuts import render,redirect
from django.views import View
from .models import Resume
from .forms import ResumeForms
# Create your views here.
class HomeView(View):
    def get(self,request):
        form=ResumeForms
        candaties=Resume.objects.all()
        return render(request,'myapp/home.html',{'candaties':candaties,'form':form})
    
    def post(self,request):
        form=ResumeForms(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
        return render(request,'myapp/home.html',{'form':form})    
    
class CandidateView(View):
    def get(self,request,pk):
        candidate=Resume.objects.get(pk=pk)
        
        return render(request,'myapp/candidate.html',{'candidate':candidate})    