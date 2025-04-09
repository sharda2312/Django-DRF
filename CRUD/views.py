from django.shortcuts import render
from rest_framework.decorators import api_view
from .serialiser import studentserialiser
from django.http import JsonResponse 
from serialisation.models import Student
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
import io

@api_view(["GET","POST","PUT", "DELETE"])
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
    
    if request.method == "PUT":
        stu = request.data
        id = stu['id']
        stu_data = Student.objects.get(id = id)
        data = studentserialiser(instance=stu_data,data=stu, partial =True)
        if data.is_valid():
            data.save()
            print("data saved")
            return Response({"hi":"hello"})
        return Response({"hi":"hello"})
    
    
    if request.method == "DELETE":
        id = request.data["id"]
        stu = Student.objects.get(id = id)
        stu.delete()
        print("data deleted")
        return Response({"hi":"hello"})
    
    
    
"""
if method.request == "GET":
    id = request.GET.get("id")
    stu = Student.objects.get(id = id)
    serial = studentseriliser(data=stu, safe=false)
    return response(serial)
    
if method.request = "POST":
    stu = request.data
    serial = studentserialiser(data=stu)
    if serial.is_valid():
        serial.save()
        
if method.request = "put":
    data = request.data
    id = stu["data"]
    stu = student.objects.get(id = id)
    serial = studentserialiser(instance = stu, data = data, partial=True)
    if serial.is_valid():
        serial.save()

"""