from django.shortcuts import render, redirect
from .forms import TodoForm
from .models import Todo
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
import random

# Create your views here.
@login_required
def home(request):
    print('home')
    tasks = Todo.objects.filter(user=request.user)
        # ページネーション用に取得
    items = Todo.objects.filter(user=request.user).order_by('id')
    # ページネーション設定
    page_size = 3
    paginator = Paginator(items, page_size)
    # 今どのページかを表示するために取得
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number) 

    return render(request, 'task_app/home.html', {'page_obj': page_obj, 'tasks': tasks})

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
        if request.method == "POST":
            # 理解度のみを更新
            understanding = request.POST.get('understanding_status')
            if understanding:
                task.understanding_status = understanding
                task.save()
            
            # 現在のタスク以外のランダムなタスクを取得
            other_tasks = Todo.objects.filter(user=request.user).exclude(id=task_id)
            if other_tasks.exists():
                random_task = random.choice(list(other_tasks))
                return redirect('solve_task', task_id=random_task.id)
            return redirect('home')
        else:
            form = TodoForm(instance=task)
            return render(request, 'task_app/solve_task.html', {'task': task, 'form': form})