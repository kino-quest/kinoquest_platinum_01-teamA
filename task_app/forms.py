from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['task_name', 'task_answer', 'understanding_status', 'category_id']
        widgets = {
          'understanding_status': forms.RadioSelect, 
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ''

        # プレースホルダーやクラスの設定
        self.fields['task_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': '問題を入力してください',
            'rows': 1
        })
        self.fields['task_answer'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': '解答を入力してください',
            'rows': 1
        })

        # ラベルの設定
        self.fields['task_name'].label = 'タスク名'
        self.fields['task_answer'].label = 'タスクの答え'
        self.fields['understanding_status'].label = '理解度'
        self.fields['category_id'].label = 'カテゴリー'