from django import forms
from .models import student_Data

class Forms_data(forms.Form):
    class Meta:
        model=student_Data
        fields='__all__'
        

