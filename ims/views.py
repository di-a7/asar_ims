from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Department
from .serializer import DepartmentSerializer
# Create your views here.

@api_view(['GET'])
def list_departments(requests):
   department = Department.objects.all()
   serializer = DepartmentSerializer(department, many=True)
   return Response(serializer.data)

# ProductCategory