from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Course, Comment, Like_course, Like, Profile
from .forms import CourseForm, CommentForm, SignupForm, SigninForm, ProfileForm
from django.contrib.auth.models import User
from django.contrib import auth
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    crs = Course.objects.all().order_by('-date')
    return render(request, 'sgapp/home.html', {'crs':crs})

def new(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            crs = form.save(commit=False)
            crs.author = request.user
            crs.save()
            return redirect('/'+str(crs.id))
    else:
        form = CourseForm()
        return render(request, 'sgapp/new.html',{'crs':form})

def detail(request, crs_id):
    crs = get_object_or_404(Course, pk=crs_id)
    form = CommentForm()
    cmt = Comment.objects.filter(crs=crs).order_by('-date')
    lk = Like_course.objects.filter(course=crs, author=request.user)
    alk = Like_course.objects.filter(course=crs)
    return render(request, 'sgapp/detail.html', {'cmt':cmt,'crs':crs, 'cform':form, 'lk':lk, 'alk':alk})

def edit(request, crs_id):
    crs = get_object_or_404(Course, pk=crs_id)
    if request.method == "POST":
        form = CourseForm(request.POST, instance=crs)
        if form.is_valid():
            c = form.save(commit=False)
            c.save()
            return redirect('detail', crs_id=c.id)
    else:
        form = CourseForm(instance=crs)
        return render(request, 'sgapp/edit.html', {'crs':form})

def delete(request, crs_id):
    crs = get_object_or_404(Course, pk=crs_id)
    crs.delete()
    return redirect('home')

def c_create(request, crs_id):
    crs = get_object_or_404(Course, pk=crs_id)
    cform = CommentForm(request.POST)
    score = request.POST['score']
    if cform.is_valid():
        cmt = cform.save(commit=False)
        cmt.score = score
        cmt.crs = crs
        cmt.author = request.user
        cmt.save()
    return redirect('detail', crs_id=crs.id)

def search(request):
    s = request.GET['search']
    c = request.GET['cate']
    sc = {f"{c}__contains":s}
    if s:
        crs = Course.objects.filter(**sc)
        return render(request, 'sgapp/search.html', {'crs':crs,'s':s})

def like(request, crs_id):
    crs = get_object_or_404(Course, pk=crs_id)
    like = Like(like=True)
    like.save()
    lc = Like_course(
        like = like,
        course = crs,
        author = request.user
    )
    lc.save()
    return redirect('detail', crs_id=crs.id)

def unlike(request, crs_id):
    crs = get_object_or_404(Course, pk=crs_id)
    like = get_object_or_404(Like_course, course=crs, author=request.user)
    like.like.delete()
    return redirect('detail', crs_id=crs.id)

def signup(request):#역시 GET/POST 방식을 사용하여 구현한다.
    if request.method == "GET":
        return render(request, 'sgapp/signup.html', {'f':SignupForm()} )
        
    elif request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['password'] == form.cleaned_data['password_check']:
                new_user = User.objects.create_user(form.cleaned_data['username'],form.cleaned_data['email'],form.cleaned_data['password'])
                new_user.last_name = form.cleaned_data['last_name']
                new_user.first_name = form.cleaned_data['first_name']
                new_user.save()
                auth.login(request, new_user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return render(request, 'sgapp/signup.html',{'f':form, 'error':'비밀번호와 비밀번호 확인이 다릅니다.'})#password와 password_check가 다를 것을 대비하여 error를 지정해준다.
        return render(request, 'sgapp/signup.html',{'f':form})
def signin(request):#로그인 기능
    if request.method == "GET":
        return render(request, 'sgapp/signin.html', {'f':SigninForm()} )

    elif request.method == "POST":
        form = SigninForm(request.POST)
        id = request.POST.get('username')
        pw = request.POST.get('password')
        u = authenticate(username=id, password=pw)
        if u: #u에 특정 값이 있다면
            login(request, user=u) #u 객체로 로그인해라
            return HttpResponseRedirect(reverse('home'))
        else:
            return render(request, 'sgapp/signin.html',{'f':form, 'error':'아이디나 비밀번호가 일치하지 않습니다.'})

from django.contrib.auth import logout #logout을 처리하기 위해 선언

def signout(request): #logout 기능
    logout(request) #logout을 수행한다.
    return HttpResponseRedirect(reverse('signin'))

def mypage(request):
    pf = Profile.objects.all()
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            pform = ProfileForm()
            return render(request, 'sgapp/mypage.html', {'pf':pf, 'pform':pform})

    else:
        form = ProfileForm()
        return render(request, 'sgapp/mypage.html', {'form':form})

#def create(request):
    # 생략
  #profile.photo = request.FILES['photo']