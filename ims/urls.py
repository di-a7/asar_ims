from django.urls import path, include
from .views import departments, department
urlpatterns = [
   path('departments/', departments),
   path('departments/<id>/', department),
]
