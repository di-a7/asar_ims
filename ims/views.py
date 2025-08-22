from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Department
from .serializer import DepartmentSerializer
from rest_framework import status
# Create your views here.

@api_view(['GET','POST'])
def departments(request):
   if request.method == 'GET':
      department = Department.objects.all()
      serializer = DepartmentSerializer(department, many=True)
      return Response(serializer.data)
   elif request.method == 'POST':
      serializer = DepartmentSerializer(data = request.data)
      serializer.is_valid(raise_exception=True)
      serializer.save()
      return Response(serializer.data, status =status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def department(request,id):
   department = Department.objects.get(id = id)
   if request.method == 'GET':
      serializer = DepartmentSerializer(department)
      return Response(serializer.data)
   
   elif request.method == 'DELETE':
      department.delete()
      return Response({
         "detail":"Category Deleted."
      }, status=status.HTTP_204_NO_CONTENT)
   
   elif request.method == 'PUT':
      serializer = DepartmentSerializer(department ,data = request.data)
      serializer.is_valid(raise_exception=True)
      serializer.save()
      return Response(serializer.data)

# ProductCategory