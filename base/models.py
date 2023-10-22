from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class UserAdditionalInfo(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key=True)
    avt = models.ImageField(null=True, blank=True, upload_to='images/')
    bg = models.ImageField(null=True, blank=True, upload_to='images/')
    dob = models.DateTimeField(null=True, blank=True)
    gender = models.CharField(null=True, max_length=10, blank=True, default="None")
    location = models.CharField(null=True, max_length=255, blank=True)
    description = models.TextField(null=True, blank=True)


class Post(models.Model):
    body = models.TextField()
    img = models.ImageField(null=True, blank=True, upload_to='images/') 
    created_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    likes = models.ManyToManyField(User, blank = True, related_name = 'likes')
    dislikes = models.ManyToManyField(User, blank = True, related_name = 'dislikes')


class Comment(models.Model):
    comment = models.TextField()
    created_on = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    post = models.ForeignKey('Post', on_delete = models.CASCADE)