from django.shortcuts import render, redirect
from .models import Post
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .import forms

def homepage(request):
    posts = Post.objects.all().order_by('date')
    return render(request,'homepage/homepage.html',{'posts': posts})
   
def postdetails(request, slug):
    post=Post.objects.get(slug=slug)
    return render(request,'homepage/postdetails.html',{'post':post})

def editpost(request,slug):
    post = Post.objects.get(slug=slug) 
    if request.method == 'POST':
        form = forms.EditPost(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('http://127.0.0.1:8000/homepage/')
    else:
        form = forms.EditPost(instance=post)
    return render(request, 'homepage/editpost.html', {'form': form})

@login_required(login_url="/users/login/")
def newpost(request):
    if request.method =='POST':
        form = forms.writepost(request.POST,request.FILES)
        if form.is_valid():
            profile= form.save(commit=False)
            profile.writer= request.user
            profile.save()
            return redirect('http://127.0.0.1:8000/homepage/')
    else:
        form = forms.writepost()
    return render(request,'homepage/newpost.html',{'form': form })






