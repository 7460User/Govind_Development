from django import forms
from .models import Resume
GANDER_CHOICE = [
    ('Male','Male'),
    ('Female','Female'),
]

JOB_CITY_CHOICE = [
    ('pune','pune'),
    ('mumbai','mumbai'),
    ('chennai','chennai'),
    ('bangolore','bangolore'),
    ('delhi','delhi'),

]


class ResumeForms(forms.ModelForm):
    gender = forms.ChoiceField(choices=GANDER_CHOICE,widget=forms.RadioSelect)
    job_city =forms.MultipleChoiceField(label='prefected jobs locations',choices=JOB_CITY_CHOICE,widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Resume
        fields =  ['id','name','dob','gender','locality',
                    'city','pin','state','mobile','email','job_city','profile_image',
                    'my_file',] 

        labels ={ 'name':'full Name','dob':'date of Birth','pin':'pin code',
                    'mobile':'mobile N','email':'Email ID',
                    'profile_image':'Profile image ','my_file':'Document'}

        widgets = {


            'name' :forms.TextInput(attrs={'class':'form-control'}),
            'dob':forms.DateInput(attrs={'class':'form-control','id':'datepicker'}),
            'locality':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'pin':forms.TextInput(attrs={'class':'form-control'}),
            'state':forms.Select(attrs={'class':'form-control'}),
            'mobile':forms.NumberInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
        }