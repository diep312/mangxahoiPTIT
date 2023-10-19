from django.contrib import admin
from .models import Post, Comment
from .models import User

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(User)
