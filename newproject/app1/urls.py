from django.contrib import admin
from django.urls import path,include
from .views import employee_table
from rest_framework import routers


router=routers.DefaultRouter()
router.register(r'api',employee_table)


urlpatterns = [
    path('',include(router.urls))

]