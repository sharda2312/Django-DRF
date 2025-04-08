from django.shortcuts import render
from rest_framework import response
from .models import Student
from rest_framework.decorators import api_view
import io
from .serialiser import studentserialiser
from rest_framework.parsers import JSONParser
# Create your views here.

@api_view(["post"])
def de_stu_info(request):
    data = request.data
    serialiser = studentserialiser(data = data)
    if serialiser.is_valid():
        serialiser.save()
        
    
