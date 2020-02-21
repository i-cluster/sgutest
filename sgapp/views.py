from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Course, Comment, Like_course, Like
from .forms import CourseForm, CommentForm

# Create your views here.

def home(request):
    crs = Course.objects.all()
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
    cmt = Comment.objects.filter(crs=crs)
    like = Like_course.objects.filter(course=crs)
    return render(request, 'sgapp/detail.html', {'cmt':cmt,'crs':crs, 'cform':form, 'like':like})

def edit(request, crs_id):
    crs = get_object_or_404(Course, pk=crs_id)
    if request.method == "POST":
        form = CourseForm(request.POST, instance=crs)
        if form.is_valid():
            c = form.save(commit=False)
            c.author = request.user
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
    if cform.is_valid():
        cmt = cform.save(commit=False)
        cmt.crs = crs
        if not cform.data['author']:
            crs.author = request.user
        cmt.save()
    return redirect('detail', crs_id=crs.id)

def search(request):
    s = request.GET['search']
    c = request.GET['cate']
    sc = {f"{c}__contains":s}
    if s:
        crs = Course.objects.filter(**sc)
        return render(request, 'sgapp/search.html', {'crs':crs})

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