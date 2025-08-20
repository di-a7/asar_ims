from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
   list_display = ['id', 'name']
   search_fields = ['name']

class ProductCategoryAdmin(admin.ModelAdmin):
   list_display = ['id', 'name']
   search_fields = ['name']

admin.site.register(ProductCategory,ProductCategoryAdmin)

class ProductsAdmin(admin.ModelAdmin):
   list_display = ['id', 'name', 'stock']
   search_fields = ('name','category__name', 'department__name')
   list_filter = ['category__name', 'department__name', 'stock']
   autocomplete_fields = ['category','department']
   
admin.site.register(Products,ProductsAdmin)
admin.site.register(Supplier)
admin.site.register(Purchase)
admin.site.register(PurchaseItem)

# supplier ko admin