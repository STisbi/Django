from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import BlogUser

# Register your models here.
admin.site.register(BlogUser, UserAdmin)