from django.urls import path, include
from .views import list_departments
urlpatterns = [
   path('departments/', list_departments)
]
