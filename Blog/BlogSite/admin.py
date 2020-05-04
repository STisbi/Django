from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import BlogUser, Blog, Comment, Document, VoteRecord

# Register your models here.
admin.site.register(BlogUser, UserAdmin)
admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(Document)
admin.site.register(VoteRecord)

UserAdmin.fieldsets += (
    ('Custom Fields', {'fields': ('biography',)}),
)