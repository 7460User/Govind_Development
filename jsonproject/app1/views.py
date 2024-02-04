from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
def employee_data_jsondirectview(request):
    employee_data={'eno':101,'ename':'Naresh','esal':12.00,'eddr':'hyderabad'}
    return JsonResponse(employee_data)