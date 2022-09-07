from ast import Or
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import CommentForm,FeedbackForm
from .models import Post, subscriber
from django.contrib import messages

def frontpage(request):
    if request.method == "GET":
        posts = Post.objects.all()
        return render(request, 'blog/frontpage.html', {'posts': posts})
    else:
        email = request.POST['email']
        b=subscriber(email=email)
        b.save()
        messages.success(request,'Your subscription is successful')
        posts = Post.objects.all()
        return render(request, 'blog/frontpage.html', {'posts': posts})

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    npost= Post.objects.all()[:5]
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = CommentForm()
    return render(request, 'blog/post_detail.html', {'post': post, 'form': form,'npost':npost})

def technical(request):
    posts = Post.objects.filter(field='technical').values()
    print(posts)
    return render(request, 'blog/frontpage.html', {'posts': posts})

def hotpost(request):
    posts = Post.objects.filter(field='hot').values()
    print(posts)
    return render(request, 'blog/frontpage.html', {'posts': posts})

def entertainment(request):
    posts = Post.objects.filter(field='entertainment').values()
    print(posts)
    return render(request, 'blog/frontpage.html', {'posts': posts})

def science(request):
    posts = Post.objects.filter(field='science').values()
    print(posts)
    return render(request, 'blog/frontpage.html', {'posts': posts})

def lifehacks(request):
    posts = Post.objects.filter(field='lifehack').values()
    print(posts)
    return render(request, 'blog/frontpage.html', {'posts': posts})

def subscribe(request):
    if request.method == "GET":
        posts = Post.objects.all()
        return render(request, 'blog/frontpage.html', {'posts': posts})

    else:
        email = request.POST['email']
        b=subscriber(email=email)
        b.save()
        posts = Post.objects.all()
        return render(request, 'blog/frontpage.html', {'posts': posts})

def help(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Your feedback submitted successfully')
            return render (request,'blog/help.html',{'form':form})
        messages.success(request,'Your form is invalid submit again')
        return render (request,'blog/help.html',{'form':form})
    else:
        form = FeedbackForm()
    return render (request,'blog/help.html',{'form':form})

from .models import students
from django.db.models import Q
def search(request):
    if 'q' in request.GET:
        q=request.GET['q']
        print(request.GET)
        print(q)
        s=students.objects.filter(Q(firstname__icontains=q) | Q(lastname=q) | Q(subject=q))
    else:
        s= students.objects.all()
    return render(request,'blog/search.html',{'data':s})


def one(request):
    return render(request,'blog/one.html')

def two(request):
    return render(request,'blog/two.html')

def skip1(request):
    return render(request,'blog/skip1.html')

def skip2(request):
    return render(request,'blog/skip2.html')