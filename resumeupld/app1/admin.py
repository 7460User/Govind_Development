from django.contrib import admin
from app1.models import Resume

# Register your models here.
admin.site.register(Resume)
class ResumeModelAdmin(admin.ModelAdmin):
    list_display = ['id','name','dob','gender','locality',
                    'city','pin','state','mobile','job_city','profile_image',
                    'my_file'] 