from rest_framework import serializers
from .models import *

class DepartmentSerializer(serializers.ModelSerializer):
   class Meta:
      model = Department
      # fields = '__all__'
      fields = ['id','name']
      # exclude = ['id']
   
   def save(self, **kwargs):
      validated_data = self.validated_data
      # Department.objects.filter()
      total_number = self.Meta.model.objects.filter(name = validated_data.get('name')).count()
      if total_number > 0:
         raise serializers.ValidationError("Department with this name already exists.")
      department = self.Meta.model(**validated_data)
      department.save()
      return department
   

class ProductCategorySerializer(serializers.ModelSerializer):
   class Meta:
      model = ProductCategory
      fields = ['id','name']

class ProductSerializer(serializers.ModelSerializer):
   stock_with_5 = serializers.SerializerMethodField()
   category = serializers.StringRelatedField()
   category_id = serializers.PrimaryKeyRelatedField(
      queryset = ProductCategory.objects.all(),
      source = 'category'
   )
   department_id = serializers.PrimaryKeyRelatedField(
      queryset = Department.objects.all(),
      source = 'department'
   )
   department = serializers.StringRelatedField()
   class Meta:
      model = Products
      fields = ["name","description","stock","stock_with_5","category_id","category","department_id","department"]
   
   def get_stock_with_5(self, product: Products):
      return product.stock + 5

class PurchaseItemSerializer(serializers.ModelSerializer):
   class Meta:
      model = PurchaseItem
      fields = ['product']

class PurchaseSerializer(serializers.ModelSerializer):
   user = serializers.HiddenField(default=serializers.CurrentUserDefault())
   items = PurchaseItemSerializer(many=True)
   class Meta:
      model = Purchase
      fields = ["quantity","price","supplier","user","items"]
   
   def create(self, validated_data):
      items = validated_data.pop('items')
      purchase = Purchase.objects.create(**validated_data)
      
      for item in items:
         PurchaseItem.objects.create(purchase = purchase, product = item.get('product'))
      return purchase
