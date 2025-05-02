from django.shortcuts import render
from .forms import SignupForm


# 新規登録
def signup(request):
    print("signup")
    form = SignupForm()
    params = {
        'form': form,
    }
    return render(request, 'accounts_app/signup.html', params)