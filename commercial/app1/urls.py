from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("index",views.index,name='index'),
    path("",views.index,name='index'),
    path("about",views.about,name='about'),
    path("services",views.services,name='services'),
    path('contact',views.contact,name='contact'),
    path('delete/<int:id>',views.delete),
    path('update/<int:id>',views.update,name='update'),
    path('uprec/<int:id>',views.uprec,name='uprec'),
]