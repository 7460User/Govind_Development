from .models import Resume
from django import forms


GENDER_CHOICES=[
    ('Male','Male'),
    ('Female','Female')
]
Job_City_Choices = [
    ('Delhi', 'Delhi'),
    ('Mumbai', 'Mumbai'),
    ('Bangalore', 'Bangalore'),
    ('Hyderabad', 'Hyderabad'),
    ('Chennai', 'Chennai'),
    ('Kolkata', 'Kolkata'),
    ('Pune', 'Pune'),
    ('Ahmedabad', 'Ahmedabad'),
    ('Jaipur', 'Jaipur'),
    ('Surat', 'Surat'),
]

class ResumeForms(forms.ModelForm):
    gender=forms.ChoiceField(choices=GENDER_CHOICES,widget=forms.RadioSelect)
    job_city=forms.MultipleChoiceField(label='preferred Job Locations',choices=Job_City_Choices,widget=forms.CheckboxSelectMultiple)
    class Meta:
        model=Resume
        fields='__all__'

        labels={'name':'Full Name','dob':'Date of Birth','pin':'Pin Code',
                  'mobile':'Mobile No','email':'Email Id',
                  'profile_image':'profile_image','file_image':'Document'}
        
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'dob':forms.DateInput(attrs={'class':'form-control','Id':'datepicker'}),
            'locality':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'pin':forms.TextInput(attrs={'class':'form-control'}),
            'state':forms.Select(attrs={'class':'form-control'}),
            'mobile':forms.NumberInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),

        }