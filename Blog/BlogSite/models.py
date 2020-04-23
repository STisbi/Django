from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class BlogUser(AbstractUser):
    pass


class Blog(models.Model):
    pass


class Comment(models.Model):
    pass