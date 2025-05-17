from django.shortcuts import render

# Create your views here.
def home(request):
    print("home")
    return render(request, 'task_app/home.html')

def privacy(request):
    return render(request, 'task_app/privacy.html')

def rules(request):
    return render(request, 'task_app/rules.html')