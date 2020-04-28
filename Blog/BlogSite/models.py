from datetime import date

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

from .validators import validate_file_extension


class BlogUser(AbstractUser):
    biography = models.TextField(max_length=400, help_text='Who am I?', default="I think therefore I am.")

    def get_absolute_url(self):
        return reverse('blog-list-by-author', args=[str(self.id)])


class Blog(models.Model):
    title = models.CharField(max_length=20)
    post_date = models.DateField(default=date.today())
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    entry = models.TextField(max_length=2000, help_text='What''s on your mind?')

    def get_absolute_url(self):
        return reverse('blog-detail', args=[str(self.id)])

    def __str__(self):
        return self.title


class Comment(models.Model):
    comment = models.TextField(max_length=200, help_text='What do you think?')
    post_date = models.DateField(default=date.today())

    # A blog can have multiple comments
    blog = models.ForeignKey('Blog', on_delete=models.CASCADE)

    # An author can leave multiple comments
    author = models.ForeignKey(BlogUser, on_delete=models.SET_NULL, null=True)


class Document(models.Model):
    title = models.CharField(max_length=20)

    document_1 = models.FileField(upload_to='uploads/', validators=[validate_file_extension])
    document_2 = models.FileField(upload_to='uploads/', validators=[validate_file_extension])

    document_1_name = models.CharField(max_length=20)
    document_2_name = models.CharField(max_length=20)

    document_1_desc = models.TextField(max_length=200, help_text='What is this document about?')
    document_2_desc = models.TextField(max_length=200, help_text='What is this document about?')

    upload_date = models.DateField(default=date.today())

    # An author can upload multiple documents
    author = models.ForeignKey(BlogUser, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('document-detail', args=[str(self.id)])
