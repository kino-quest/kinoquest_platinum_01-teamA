from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

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
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        
        if 'admin' in username:
            raise forms.ValidationError('ユーザー名に "admin" を含めることはできません。')
        return username