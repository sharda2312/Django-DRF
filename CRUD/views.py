from django.shortcuts import render
from rest_framework.decorators import api_view
from .serialiser import studentserialiser
from django.http import JsonResponse 
from serialisation.models import Student
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
import io

@api_view(["GET","POST"])
def student(request):
    if request.method == 'GET':
        id = request.GET.get("id")
        if id :
            data = Student.objects.get(id = id)
            serial = studentserialiser(data)
            return JsonResponse(serial.data, safe=False)
        else:
            data = Student.objects.all()
            serial = studentserialiser(data, many = True)
            return JsonResponse(serial.data, safe = False)

    if request.method == 'POST':
        data = request.data
        data = studentserialiser(data=data)
        if data.is_valid():
            data.save()
            print("data saved")
            return Response({"hi":"hello"})
        return Response({"hi":"hello"})