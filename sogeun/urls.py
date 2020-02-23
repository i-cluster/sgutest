"""sogeun URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from sgapp import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.signin, name="signin"),
    path('home/', views.home, name="home"),
    path('new', views.new, name="new"),
    path('signup/', views.signup, name="signup"),
    path('signout/', views.signout, name="signout"),
    path('signin/', views.signin, name="signin"),
    path('mypage/', views.mypage, name="mypage"),
    path('change_pw/', views.change_pw, name="change_pw"),
    path('<int:crs_id>', views.detail, name="detail"),
    path('edit/<int:crs_id>', views.edit, name="edit"),
    path('delete/<int:crs_id>', views.delete, name="delete"),
    path('c_create/<int:crs_id>', views.c_create, name="c_create"),
    path('search/', views.search, name="search"),
    path('like/<int:crs_id>', views.like, name="like"),
    path('unlike/<int:crs_id>', views.unlike, name="unlike"),
    path('follow/<int:crs_id>', views.postfollow, name="follow"),
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)