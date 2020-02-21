from django.contrib import admin
from .models import Course, Comment, Like, Like_course, Profile

# Register your models here.

admin.site.register(Course)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Like_course)
admin.site.register(Profile)