from django import forms
from .models import Todo, Category, CategoryLevel

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['task_name', 'task_answer', 'understanding_status', 'category_id']
        widgets = {
            'understanding_status': forms.RadioSelect,
            'category_id': forms.Select(attrs={
                'class': 'form-control',
                'style': 'width: 100%;'
            })
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
        
        # カテゴリーの設定
        self.fields['category_id'] = forms.ChoiceField(
            choices=[('', 'カテゴリーを選択してください')] + list(CategoryLevel.choices),
            widget=forms.Select(attrs={
                'class': 'form-control',
                'style': 'width: 100%;'
            }),
        )

    # フォームで選択された値を「Category」インスタンスに変換する
    def clean_category_id(self):
        category_value = self.cleaned_data['category_id']
        if category_value:
            # カテゴリーが存在しない場合は作成
            category, _ = Category.objects.get_or_create(category_name=int(category_value))
            return category
        return None
