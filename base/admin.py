from django.contrib import admin
from .models import Post, Comment, UserAdditionalInfo
from .models import User

admin.site.register(UserAdditionalInfo)
admin.site.register(Post)
admin.site.register(Comment)

