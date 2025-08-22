from rest_framework import serializers
from .models import Department

class DepartmentSerializer(serializers.Serializer):
   id = serializers.IntegerField(read_only=True)
   name = serializers.CharField()
   
   def create(self, validated_data):
      return Department.objects.create(**validated_data)
   
   def update(self, instance, validated_data):
      instance.name = validated_data.get('name', instance.name)
      return instance