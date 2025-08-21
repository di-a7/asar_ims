from rest_framework import serializers

class DepartmentSerializer(serializers.Serializer):
   id = serializers.IntegerField()
   name = serializers.CharField()