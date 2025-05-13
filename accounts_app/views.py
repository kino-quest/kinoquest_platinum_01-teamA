from django.contrib.auth import login, logout
from django.shortcuts import redirect, render
from .forms import LoginForm, SignupForm


# 新規登録
def signup_view(request):
    print("signup")
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignupForm()
    params = {
        'form': form,
    }
    return render(request, 'accounts_app/signup.html', params)

# ログイン
def login_view(request):
    print("login")
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, 'パスワードが正しくありません。')
                params = {
                    'form': form,
                }
            return render(request, 'accounts_app/login.html', params)
        else:
            print("isn't valid")
            print(form.errors)
            params = {
                'form': form,
            }
            return render(request, 'accounts_app/login.html', params)
    else:
        form = LoginForm()
    params = {
        'form': form,
    }
    return render(request, 'accounts_app/login.html', params)