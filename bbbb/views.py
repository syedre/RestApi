from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import viewsets
#from rest_framework.response  import Response
#from rest_framework import status
from .models import Employee
from  bbbb import serializers
from .serializers import EmployeeSerializer
# Create your views here.


class EmployeeViewSet(viewsets.ModelViewSet):
	
	queryset = Employee.objects.all()
	serializer_class = EmployeeSerializer
	
