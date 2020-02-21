from  __future__ import unicode_literals
from django.db import models
from django.utils import timezone

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=50)
    prof = models.CharField(max_length=30)
    dep = models.CharField(max_length=50)
    eval = models.TextField(default="")

class Comment(models.Model):
    crs = models.ForeignKey('sogeuna.Course', on_delete=models.CASCADE, related_name='comment')
    content = models.CharField(max_length=300)
    date = models.DateTimeField(default=timezone.now)
    author = models.CharField(max_length=30, null=True, blank=True)

class Like(models.Model):
    like = models.BooleanField(default=False)

class Like_course(models.Model):
    like = models.ForeignKey('sogeuna.Like', on_delete=models.CASCADE)
    course = models.ForeignKey('sogeuna.Course', on_delete=models.CASCADE)
    author = models.CharField(max_length=30, null=True, blank=True)