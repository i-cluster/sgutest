from django import forms
from .models import Course, Comment

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'prof', 'dep', 'eval']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'author']