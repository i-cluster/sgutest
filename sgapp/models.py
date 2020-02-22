from  __future__ import unicode_literals
from django.db import models
from django.utils import timezone

# Create your models here.

class Course(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=50)
    prof = models.CharField(max_length=30)
    dep = models.CharField(max_length=50)
    eval = models.TextField(default="")
    author = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.name
    
    def summary(self):
        return self.eval[:50]

class Comment(models.Model):
    objects = models.Manager()
    crs = models.ForeignKey('sgapp.Course', on_delete=models.CASCADE, related_name='comment')
    content = models.CharField(max_length=300)
    score = models.IntegerField(default=0)
    date = models.DateTimeField(default=timezone.now)
    author = models.CharField(max_length=30, null=True, blank=True)

class Like(models.Model):
    objects = models.Manager()
    like = models.BooleanField(default=False)

class Like_course(models.Model):
    objects = models.Manager()
    like = models.ForeignKey('sgapp.Like', on_delete=models.CASCADE)
    course = models.ForeignKey('sgapp.Course', on_delete=models.CASCADE)
    author = models.CharField(max_length=30, null=True, blank=True)

class Profile(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=100)
    photo = models.ImageField(blank=True, upload_to='images/')