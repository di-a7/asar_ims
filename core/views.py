from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.serializers import ValidationError
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes
from .serializer import LoginSerializer

# Create your views here.
# User = get_user_model()

class LoginAPI(APIView):
   
   @extend_schema(
      request=LoginSerializer,
      responses={201: LoginSerializer},
      description='this is a login api',
      
   )
   def post(self, request):
      username = request.data.get('username')
      password = request.data.get('password')
      if username is None or password is None:
         raise ValidationError({"details":"Both username and password are required."})
      
      user = authenticate(username = username,password = password)
      if user:
         token,_ = Token.objects.get_or_create(user = user)
         return Response({"detail":"User login Successful.","token":token.key, "username":username})
      else:
         return Response({"detail":"The user with this username does not exists."})