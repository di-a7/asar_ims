from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'departments',DepartmentViewset, basename='departments')
router.register(r'categories',ProductCategoryViewset, basename='categories')
router.register(r'products',ProductViewset, basename='products')
router.register(r'purchases',PurchaseViewset, basename='purchases')

urlpatterns = [
   # path('departments/', departments),
   # path('departments/<id>/', department),
   # path('departments/abc/xyz/',Department.as_view({'get':'list', 'post':'create'}), name = "departments"),
   # path('departments/<pk>/',Department.as_view({'get':'retrieve','put':'update','patch':'partial_update','delete':'destroy'})),
] + router.urls
