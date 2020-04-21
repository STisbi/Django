from django.contrib.auth.models import User
from django.db import models
from datetime import date

# Create your models here.
from django.urls import reverse


class Blog(models.Model):
    title = models.CharField(max_length=20)
    post_date = models.DateField(default=date.today())
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    entry = models.TextField(max_length=2000, help_text='What''s on your mind?')

    def get_absolute_url(self):
        return reverse('blog-detail', args=[str(self.id)])

    def __str__(self):
        return self.title


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    biography = models.TextField(max_length=400, help_text='Who am I?')

    def get_absolute_url(self):
        return reverse('blog-list-by-author', args=[str(self.id)])

    def __str__(self):
        return self.user.username


class Comment(models.Model):
    comment = models.TextField(max_length=200, help_text='What do you think?')
    post_date = models.DateField(default=date.today())
    blog = models.ForeignKey('Blog', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)