from datetime import date

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


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
    blog = models.ForeignKey('Blog', on_delete=models.CASCADE)
    author = models.ForeignKey(BlogUser, on_delete=models.SET_NULL, null=True)