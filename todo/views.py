from django import forms
from django.shortcuts import render,redirect,get_object_or_404
from .models import Task
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.

from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control"})


def signup(request):
    if request.user.is_authenticated:
        return redirect("todo:task_list")

    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Account created successfully!")
            return redirect("todo:task_list")
    else:
        form = SignUpForm()
    return render(request, "todo/signup.html", {"form": form})


def signin(request):
    if request.user.is_authenticated:
        return redirect("todo:task_list")

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Signed in successfully!")
                return redirect("todo:task_list")
    else:
        form = AuthenticationForm()

    return render(request, "todo/signin.html", {"form": form})


def signout(request):
    logout(request)
    messages.success(request, "Signed out successfully!")
    return redirect("todo:signin")


@login_required(login_url="todo:signin")
def task_list(request):
    task = Task.objects.all().order_by("-created_at")
    return render(request, "todo/task_list.html", {"task": task})



def task_create(request):
    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        description = request.POST.get("description", "").strip()

        if title:
            Task.objects.create(
                title=title,
                description=description
            )
            messages.success(request, "Task added successfully!")
            return redirect("todo:task_list")
        messages.error(request, "Title cannot be empty.")
        return render(request, "todo/task_form.html", {"error":"Title cannot be empty."})

    return render(request, "todo/task_form.html")



def task_update(request,pk):
    task=get_object_or_404(Task,pk=pk)
    if request.method=='POST':
        title=request.POST.get('title','').strip()
        description=request.POST.get('description', '').strip()
        completed = request.POST.get('completed')=='on'
        if title:
            task.title=title
            task.description=description
            task.completed=completed
            task.save()
            messages.success(request, "Task updated successfully!")
            return redirect(reverse('todo:task_list'))
        messages.error(request, "Title cannot be empty.")
        return render(request, 'todo/task_form.html', {'task':task, 'error':'title cannot be empty'})
    return render(request, 'todo/task_form.html', {'task':task})



def task_delete(request,pk):
    task=get_object_or_404(Task,pk=pk)
    if request.method=='POST':
        task.delete()
        messages.success(request, "Task deleted successfully!")
        return redirect(reverse('todo:task_list'))
    return render(request,'todo/task_confirm_delete.html',{'task':task})



def task_toggle(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == "POST":
        task.completed = not task.completed
        task.save()
        status = "completed" if task.completed else "marked pending"
        messages.success(request, f"Task {status} successfully!")

    return redirect("todo:task_list")