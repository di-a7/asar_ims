from django.db import models

# Create your models here.
class Department(models.Model):
   name = models.CharField(max_length=100)
   
   def __str__(self):
      return self.name

class ProductCategory(models.Model):
   name = models.CharField(max_length=50)
   
   def __str__(self):
      return self.name

class Products(models.Model):
   name = models.CharField(max_length=100)
   description = models.TextField()
   stock = models.IntegerField()
   category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
   department = models.ForeignKey(Department, on_delete=models.CASCADE)
   
   def __str__(self):
      return self.name

class Supplier(models.Model):
   AVAILABLE = 'A'
   NOT_AVAILABLE = "N"
   CHOICES = {
      AVAILABLE : "Available",
      NOT_AVAILABLE : "Not Available"
   }
   name = models.CharField(max_length=100) 
   is_available = models.CharField(max_length=1, choices=CHOICES, default=AVAILABLE)
   
   def __str__(self):
      return self.name

class Purchase(models.Model):
   quantity = models.IntegerField()
   price = models.FloatField()
   supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
   
   def __str__(self):
      return f"Purchase id:{self.id}"

class PurchaseItem(models.Model):
   product = models.ForeignKey(Products, on_delete=models.PROTECT)
   purchase = models.ForeignKey(Purchase, on_delete=models.PROTECT)