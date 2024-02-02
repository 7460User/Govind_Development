from django.shortcuts import render

# Create your views here.
import csv
from django.http import HttpResponse
def some_view(request):
    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition':'attachment;filename="somefilename.csv"'},
    )
    writer = csv.writer(response)
    writer.writerow([101,'govind','python',4000.5])
    writer.writerow([102,'raja','python',1000.5])
    return response