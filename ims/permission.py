from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAuthenticatedorReadOnly(BasePermission):
   def has_permission(self, request, view):
      return (request.method in SAFE_METHODS) or (request.user and request.user.is_authenticated)

class IsAdmin(BasePermission):
   def has_permission(self, request, view):
      return request.user and request.user.is_authenticated and request.user.groups.filter(name="admin").exists()