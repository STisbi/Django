from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import BlogUser, Blog, Comment, Document

# Register your models here.
admin.site.register(BlogUser, UserAdmin)
admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(Document)

UserAdmin.fieldsets += (
    ('Custom Fields', {'fields': ('biography',)}),
)