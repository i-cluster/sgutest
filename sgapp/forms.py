from django import forms
from .models import Course, Comment, Profile, Tag
from django.forms import ModelForm
from django.contrib.auth.models import User

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'prof', 'dep', 'eval']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'author']

class SignupForm(ModelForm):
    password_check = forms.CharField(max_length=200, widget=forms.PasswordInput())
    field_order=['username','password','password_check','last_name','first_name','email']
    class Meta:
        model = User
        widget = {'password':forms.PasswordInput}
        fields = ['username','password','last_name','first_name','email']

class SigninForm(ModelForm):
    class Meta:
        model = User
        widgets = {'password':forms.PasswordInput}
        fields = ['username','password']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['title', 'photo', ]

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['tname']