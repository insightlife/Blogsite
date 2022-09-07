from django.contrib import admin

from .models import Post,Comment,subscriber,students

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(subscriber)
admin.site.register(students)