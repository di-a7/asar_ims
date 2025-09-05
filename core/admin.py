from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class UserAdmin(UserAdmin):
   fieldsets = (
      (None, {"fields": ("username", "password")}),
      (("Personal info"), {"fields": ("first_name", "last_name", "email","phone_number")}),
      (
         ("Permissions"),
         {
               "fields": (
                  "is_active",
                  "is_staff",
                  "is_superuser",
                  "groups",
                  "user_permissions",
               ),
         },
      ),
      (("Important dates"), {"fields": ("last_login", "date_joined")}),
   )
   list_display = ["username", "phone_number","is_staff"]

admin.site.register(User, UserAdmin)

