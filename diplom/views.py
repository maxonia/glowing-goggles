from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from portal.models import Task
from portal.forms import CustomUserCreationForm
from datetime import datetime
from django.http import HttpResponse
from portal.forms import TaskForm
from datetime import date
from django.urls import reverse

def index(request):
    selected_date = request.GET.get('date') or date.today().isoformat()
    if not request.user.is_authenticated:
        tasks = []
    else:
        tasks = Task.objects.filter(
            user=request.user,
            date=selected_date
        )
    return render(request, 'index.html', {
        'tasks': tasks,
        'selected_date': selected_date
    })

def add_event(request):
    # Ваш код для добавления события
    return render(request, 'assistant_app/add_event.html')

def home(request):
    return HttpResponse("Hello from diplom app!")

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # или другой адрес
        else:
            return render(request, 'login.html', {'error': 'Неверный логин или пароль'})
    return render(request, 'login.html')

def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")  # или куда надо
    else:
        form = CustomUserCreationForm()
    return render(request, "register.html", {"form": form})

def tasks_view(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('tasks')  # Имя урла со списком задач
    else:
        form = TaskForm()
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'portal/tasks.html', {'form': form, 'tasks': tasks})

def delete_task(request, task_id):
    if request.method == "POST":     # безопасность!
        task = get_object_or_404(Task, id=task_id)
        task.delete()
    return redirect(reverse('tasks'))  # или куда нужно тебя вернуть

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def main_view(request):
    date_str = request.GET.get('date')
    if date_str:
        try:
            selected_date = datetime.strptime(date_str, '%Y-%m-%d').date()
        except ValueError:
            selected_date = datetime.today().date()
    else:
        selected_date = datetime.today().date()

    user_tasks = Task.objects.filter(owner=request.user, due_date=selected_date).order_by('priority')
    context = {
        'selected_date': selected_date,
        'tasks': user_tasks,
    }
    return render(request, 'main.html', context)


@login_required
def tasks_view(request):
    user = request.user
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = user
            task.save()
            return redirect('tasks')
    else:
        form = TaskForm()
    tasks = Task.objects.filter(user=user).order_by('date')
    return render(request, 'assistant_app/tasks.html', {'form': form, 'tasks': tasks})

@login_required
def profile(request):
    return render(request, 'profile.html', {
        'user': request.user
    })
def profile_view(request):
    # Здесь можно добавить логику, например, передать request.user в шаблон
    return render(request, 'profile.html', {'user': request.user})




