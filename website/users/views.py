from django.shortcuts import render,redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def userform(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('http://127.0.0.1:8000/homepage/newpost')
    else:
        form=UserCreationForm()
    return render (request,'users/signin.html', {'form':form})

def loginform(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('http://127.0.0.1:8000/homepage/')
    else:
        form= AuthenticationForm()
    return render(request,'users/login.html',{'form':form})

def logoutform(request):
    if request.method =='POST':
        logout(request)
        return redirect('http://127.0.0.1:8000/homepage/')



