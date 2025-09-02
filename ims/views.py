from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializer import DepartmentSerializer, ProductCategorySerializer, ProductSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.serializers import ValidationError
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter
# Create your views here.

class DepartmentViewset(ModelViewSet):
   queryset = Department.objects.all()
   serializer_class = DepartmentSerializer


class ProductCategoryViewset(ModelViewSet):
   queryset = ProductCategory.objects.all()
   serializer_class = ProductCategorySerializer
   
   def destroy(self, request, *args, **kwargs):
      category = self.get_object()
      order_item = PurchaseItem.objects.filter(product__category = category).count()
      if order_item > 0:
         raise ValidationError({
            "details":"Purchase item has the product of this category. This cannot be deleted."
         })
      category.delete()
      return Response({
         "details":"The category has been deleted."
      })

class ProductViewset(ModelViewSet):
   queryset = Products.objects.select_related('category','department').all()
   serializer_class = ProductSerializer
   pagination_class = PageNumberPagination
   filter_backends = [SearchFilter]
   search_fields = ['name','stock']



# Generic, Mixin

# class DepartmentList(ListCreateAPIView):
#    queryset = Department.objects
#    serializer_class = DepartmentSerializer

# class DepartmentDetail(RetrieveUpdateDestroyAPIView):
#    queryset = Department.objects.all()
#    serializer_class = DepartmentSerializer
#    lookup_field = 'pk'





## APIView
# class DepartmentList(APIView):

   # def get(self, request):
   #    department = self.queryset.all()
   #    serializer = DepartmentSerializer(department, many=True)
   #    return Response(serializer.data)

   # def post(self, request):
   #    serializer = DepartmentSerializer(data = request.data)
   #    serializer.is_valid(raise_exception=True)
   #    serializer.save()
   #    return Response(serializer.data, status =status.HTTP_201_CREATED)


# class DepartmentDetail(APIView):
   
#    def get(self, request, id):
#       department = Department.objects.get(id = id)
#       serializer = DepartmentSerializer(department)
#       return Response(serializer.data)
   
#    def delete(self, request, id):
#       department = Department.objects.get(id = id)
#       department.delete()
#       return Response({"detail":"Category Deleted."}, status=status.HTTP_204_NO_CONTENT)
   
#    def put(self, request, id):
#       department = Department.objects.get(id = id)
#       serializer = DepartmentSerializer(department ,data = request.data)
#       serializer.is_valid(raise_exception=True)
#       serializer.save()
#       return Response(serializer.data)



# Function Based API:

# @api_view(['GET','POST'])
# def departments(request):
#    if request.method == 'GET':
#       department = Department.objects.all()
#       serializer = DepartmentSerializer(department, many=True)
#       return Response(serializer.data)
#    elif request.method == 'POST':
#       serializer = DepartmentSerializer(data = request.data)
#       serializer.is_valid(raise_exception=True)
#       serializer.save()
#       return Response(serializer.data, status =status.HTTP_201_CREATED)

# @api_view(['GET','PUT','DELETE'])
# def department(request,id):
#    department = Department.objects.get(id = id)
#    if request.method == 'GET':
#       serializer = DepartmentSerializer(department)
#       return Response(serializer.data)
   
#    elif request.method == 'DELETE':
#       department.delete()
#       return Response({
#          "detail":"Category Deleted."
#       }, status=status.HTTP_204_NO_CONTENT)
   
#    elif request.method == 'PUT':
#       serializer = DepartmentSerializer(department ,data = request.data)
#       serializer.is_valid(raise_exception=True)
#       serializer.save()
#       return Response(serializer.data)

# ProductCategory