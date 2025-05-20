from django.contrib import messages
from django.contrib.auth import update_session_auth_hash, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .forms import LoginForm, SignupForm, CustomPasswordChangeForm, UserUpdateForm


# 新規登録
def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')    
    else:
        form = SignupForm()
    return render(request, 'accounts_app/signup.html', {'form': form})

# ログイン
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user is not None:
                login(request, user)
                return redirect('home')
            #ログイン失敗
            form.add_error(None, 'ログインに失敗しました')
        #バリデーション失敗 or ユーザーがNoneのどちらもここで処理
        return render(request, 'accounts_app/login.html', {'form': form})
    else:
        form = LoginForm()
    return render(request, 'accounts_app/login.html', {'form': form})

#ログアウト
@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

#ユーザー情報設定
@login_required
def user_settings(request):
    #すべての項目を埋めて「更新」ボタンが押された時
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        password_form = CustomPasswordChangeForm(user=request.user, data=request.POST)

        user_valid = user_form.is_valid()
        password_valid = password_form.is_valid()

        if user_valid:
            user_form.save()
        
        if password_valid:
            user = password_form.save()
            #パスワード変更後にログアウトされるのを防ぐ
            update_session_auth_hash(request, user)
        if not user_valid and not password_valid:
            messages.error(request, '入力内容に誤りがあります。確認してください')
        # どちらも成功していたら「/user_settings」へリダイレクト
        if user_valid and password_valid:
            messages.success(request, 'ユーザー情報を更新しました')
            return redirect('user_settings')
    else:
        user_form = UserUpdateForm(instance=request.user)
        password_form = CustomPasswordChangeForm(user=request.user)
    
    params = {
        'user_form': user_form,
        'password_form': password_form,
    }
    return render(request, 'accounts_app/user_info.html', params)
