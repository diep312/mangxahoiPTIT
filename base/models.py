from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class User(models.Model):
    userName = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    # friendLists = 
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    


class Post(models.Model):
    body = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    likes = models.ManyToManyField(User, blank = True, related_name = 'likes')
    dislikes = models.ManyToManyField(User, blank = True, related_name = 'dislikes')


class Comment(models.Model):
    comment = models.TextField()
    created_on = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    post = models.ForeignKey('Post', on_delete = models.CASCADE)