from django.shortcuts import render, redirect
from .forms import TodoForm
from .models import Todo

# Create your views here.
def home(request):
    print('home')
    tasks = Todo.objects.filter(user=request.user)
    return render(request, 'task_app/home.html', {'tasks': tasks})

def privacy(request):
    return render(request, 'task_app/privacy.html')

def rules(request):
    return render(request, 'task_app/rules.html')

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

def edit_task(request, task_id):
    task = Todo.objects.get(id=task_id)
    return render(request, 'task_app/edit_task.html', {'task': task})

def delete_task(request, task_id):
    task = Todo.objects.get(id=task_id)
    task.delete()
    return redirect('home')

def solve_task(request, task_id):
    task = Todo.objects.get(id=task_id)
    return render(request, 'task_app/solve_task.html', {'task': task})

