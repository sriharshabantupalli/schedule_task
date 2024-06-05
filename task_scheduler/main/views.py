from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, TaskForm
from .models import Task


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('add_task')
    return render(request, 'main/login.html')

def homepage(request):
    if request.user.is_authenticated:
        tasks = Task.objects.filter(assigned_to=request.user)
        return render(request, 'main/dashboard.html', {'tasks': tasks})
    else:
        tasks = Task.objects.all()
        return render(request, 'main/homepage.html', {'tasks': tasks})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('homepage')
    else:
        form = UserRegisterForm()
    return render(request, 'main/register.html', {'form': form})

@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.created_by = request.user
            task.save()
            return redirect('homepage')
    else:
        form = TaskForm()
    return render(request, 'main/add_task.html', {'form': form})
