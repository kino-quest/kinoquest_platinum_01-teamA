from django.shortcuts import render, redirect
from .forms import TodoForm
from django.contrib import messages

# Create your views here.
def home(request):
    print("home")
    return render(request, 'task_app/home.html')

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