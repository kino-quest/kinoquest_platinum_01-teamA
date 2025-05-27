from django.shortcuts import render, redirect
from .forms import TodoForm
from .models import Todo
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    print('home')
    tasks = Todo.objects.filter(user=request.user)
    return render(request, 'task_app/home.html', {'tasks': tasks})

# プライバシーポリシー
def privacy(request):
    return render(request, 'task_app/privacy.html')

# 利用規約
def rules(request):
    return render(request, 'task_app/rules.html')

# 問題作成
def add_task(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            print("form.is_valid()")
            todo = form.save(commit=False)
            todo.user = request.user
            print("save")
            todo.save()
            return redirect('home')
    else:
        form = TodoForm()
    return render(request, 'task_app/add_task.html', {'form': form})

# 問題編集
def update_task(request, task_id):
    if request.method == "POST":
        task = Todo.objects.get(id=task_id)
        form = TodoForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        task = Todo.objects.get(id=task_id)
        form = TodoForm(instance=task)
    return render(request, 'task_app/update_task.html', {'form': form, 'task': task})

# 問題削除
def delete_task(request, task_id):
    task = Todo.objects.get(id=task_id)
    task.delete()
    return redirect('home')

# 問題解く
def solve_task(request, task_id):
    task = Todo.objects.get(id=task_id)
    return render(request, 'task_app/solve_task.html', {'task': task})

