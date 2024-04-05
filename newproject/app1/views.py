from django.shortcuts import render
from .models import student_Data
from app1.serializers import serializers_data
from .forms import Forms_data
from rest_framework import viewsets
# Create your views here.

class employee_table(viewsets.ModelViewSet):
    queryset=student_Data.objects.all()
    serializer_class=serializers_data

