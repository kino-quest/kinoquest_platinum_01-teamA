from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class SignupForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ''

        self.fields['username'].label = 'ユーザー名'
        self.fields['username'].widget.attrs['placeholder'] = 'ユーザー名を入力してください'

        self.fields['email'].label = 'メールアドレス'
        self.fields['email'].widget.attrs['placeholder'] = 'メールアドレスを入力してください'

        self.fields['password1'].label = 'パスワード'
        self.fields['password1'].widget.attrs['placeholder'] = 'パスワードを入力してください'

        self.fields['password2'].label = '確認用パスワード'
        self.fields['password2'].widget.attrs['placeholder'] = '確認用パスワードを入力してください'