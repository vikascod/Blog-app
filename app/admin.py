from django.contrib import admin
from app.models import Post, Category, Profile, Comment


admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Profile)
admin.site.register(Comment)