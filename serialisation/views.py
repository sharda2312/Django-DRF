from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Student
from .serialiser import studentserialiser
from rest_framework.renderers import JSONRenderer
from django.http import JsonResponse
 

# Create your views here.

@api_view(["get"])
def stu_detail(request, pk):
    stu = Student.objects.get(id = pk)
    serial = studentserialiser(stu)
    
    return JsonResponse(serial.data)