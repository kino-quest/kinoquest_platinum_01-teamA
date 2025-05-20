from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, UserCreationForm

#新規登録
class SignupForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ''

        field_settings = {
            'username': 'ユーザー名を入力してください',
            'email': 'メールアドレスを入力してください',
            'password1': 'パスワードを入力してください',
            'password2': '確認用パスワードを入力してください',
        }

        for field_name, placeholder in field_settings.items():
            field = self.fields[field_name]
            field.widget.attrs['class'] = 'form-control w-40'
            field.widget.attrs['placeholder'] = placeholder
        
        self.fields['username'].label = 'ユーザー名'
        self.fields['email'].label = 'メールアドレス'
        self.fields['password1'].label = 'パスワード'
        self.fields['password2'].label = '確認用パスワード'

#ログイン
class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ''

        field_settings = {
            'username': 'ユーザー名を入力してください',
            'password': 'パスワードを入力してください',
        }

        for field_name, placeholder in field_settings.items():
            field = self.fields[field_name]
            field.widget.attrs['class'] = 'form-control w-40'
            field.widget.attrs['placeholder'] = placeholder

        self.fields['username'].label = 'ユーザー名'
        self.fields['password'].label = 'パスワード'
    
    #もし「admin」という文字を含むのを禁止したい場合に使用するメソッド
    def clean_username(self):
        username = self.cleaned_data.get('username')
        
        if 'admin' in username:
            raise forms.ValidationError('ユーザー名に "admin" を含めることはできません。')
        return username

#編集 ユーザー名、メールアドレスのカスタマイズ
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email']
    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        self.label_suffix = ''
    
        if user:
            self.fields['username'].widget.attrs['placeholder'] = f"{user.username}"
            self.fields['email'].widget.attrs['placeholder'] = f"{user.email}"

        for field_name in ['username', 'email']:
            self.fields[field_name].widget.attrs['class'] = 'form-control w-40'

        self.fields['username'].label = 'ユーザー名'
        self.fields['email'].label = 'メールアドレス'

#編集 PasswordChangeFormをカスタマイズ(オーバーライド)
class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ''

        field_settings = {
            'old_password': '現在のパスワードを入力してください',
            'new_password1': '新しいパスワードを入力してください',
            'new_password2': '確認用の新しいパスワードを入力してください',
        }

        for field_name, placeholder in field_settings.items():
            field = self.fields[field_name]
            field.widget.attrs['class'] = 'form-control w-40'
            field.widget.attrs['placeholder'] = placeholder

        self.fields['old_password'].label = '現在のパスワード'
        self.fields['new_password2'].label = '新しいパスワード確認'