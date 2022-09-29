from multiprocessing import context
import re
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from todolist.models import ToDoList
from .forms import ToDo, updateToDo
import datetime
# Create your views here.

@login_required(login_url='/todolist/login')
def show_todolist(request):
    data = ToDoList.objects.filter(user=request.user)
    context = {
        'tasks':data
    }
    return render(request,"todolist.html",context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created!')
            return redirect('todolist:login_user')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('todolist:show_todolist'))
        else:
            messages.info(request, 'Please recheck your login credential')
    
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    messages.success(request, 'Logged Out')
    logout(request)
    return redirect('todolist:login_user')

@login_required(login_url='/todolist/login')
def create_task(request):
    if request.method == 'POST':
        todo = ToDo(request.POST)
        if todo.is_valid():
            newtodo = ToDoList(
                user = request.user,
                date = datetime.datetime.now(),
                title = todo.cleaned_data['name'],
                description = todo.cleaned_data['description']
            )
            newtodo.save()
            return redirect('todolist:show_todolist')
    
    todo = ToDo()
    context = {
        'form':todo
    }

    return render(request, 'create_task.html',context)

@login_required(login_url='/todolist/login/')
def deletion(request, id):
    qs = ToDoList.objects.get(id=id)
    if request.method == 'POST':
        qs.delete()
        return redirect('todolist:show_todolist')
    context = {
        'todo': qs
    }
    return render(request, 'delete.html', context)

@login_required(login_url='/todolist/login/')
def update(request, id):
    qs = ToDoList.objects.get(id=id)
    todo = updateToDo(instance=qs)
    if request.method == 'POST':
        todo = updateToDo(request.POST, instance=qs)
        if todo.is_valid():
            todo.save()
            return redirect('todolist:show_todolist')
    context = {
        'todo':todo
    }
    return render(request, 'update.html', context)
    