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
        choices = [('', 'カテゴリーを選択してください')] + list(CategoryLevel.choices)
        # 更新の場合(Update)
        if self.instance and self.instance.pk:  
            initial_category = str(self.instance.category_id.category_name) if self.instance.category_id else None
            self.fields['category_id'] = forms.ChoiceField(
                choices=choices,
                initial=initial_category,
                widget=forms.Select(attrs={
                    'class': 'form-control',
                    'style': 'width: 100%;'
                })
            )
            # 初期値を上書き　フォームの初期値とフィールドの初期値が一致させるため
            self.initial['category_id'] = initial_category
            
        # 新規作成の場合(Create)
        else:  
            self.fields['category_id'] = forms.ChoiceField(
                choices=choices,
                widget=forms.Select(attrs={
                    'class': 'form-control',
                    'style': 'width: 100%;'
                })
            )

    # フォームで選択された値を「Category」インスタンスに変換する
    def clean_category_id(self):
        category_value = self.cleaned_data['category_id']
        if category_value:
            # カテゴリーが存在しない場合は作成
            category, _ = Category.objects.get_or_create(category_name=int(category_value))
            return category
        return None
