from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import BlogUser, Blog, Comment

# Register your models here.
admin.site.register(BlogUser, UserAdmin)
admin.site.register(Blog)
admin.site.register(Comment)

UserAdmin.fieldsets += (
    ('Custom Fields', {'fields': ('biography',)}),
)