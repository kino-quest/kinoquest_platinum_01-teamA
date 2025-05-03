from django.shortcuts import render
from .forms import LoginForm, SignupForm


# 新規登録
def signup(request):
    print("signup")
    form = SignupForm()
    params = {
        'form': form,
    }
    return render(request, 'accounts_app/signup.html', params)

# ログイン
def login(request):
    print("login")
    form = LoginForm()
    params = {
        'form': form,
    }
    return render(request, 'accounts_app/login.html', params)