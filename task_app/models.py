from django.db import models
from django.contrib.auth import get_user_model

# カテゴリーテーブル
class CategoryLevel(models.IntegerChoices):
    PYTHON = 1, "Python"
    CSS = 2, "CSS"
    JAVASCRIPT = 3, "JavaScript"
    TYPESCRIPT = 4, "TypeScript"
    JAVA = 5, "Java"
    C = 6, "C"
    CSHARP = 7, "C#"
    CPP = 8, "C++"
    GO = 9, "Go"

class Category(models.Model):
    category_name = models.IntegerField(choices=CategoryLevel.choices)
    
    def __str__(self):
        return self.category_name


# Todoテーブル - 理解度ステータス設定
class StatusLevel(models.IntegerChoices):
    LEVEL_1 = 1, "覚えていない"
    LEVEL_2 = 2, "うろ覚え"
    LEVEL_3 = 3, "やや不安"
    LEVEL_4 = 4, "覚えた"

# Todoテーブル
class Todo(models.Model):
    task_name = models.TextField()
    task_answer = models.TextField()
    # 理解度から参照させ、デフォルトは"1:覚えていない"とする
    understanding_status = models.IntegerField(
        choices=StatusLevel.choices, 
        default=StatusLevel.LEVEL_1
    )
    category_id = models.ForeignKey(Category, models.CASCADE, null=True)
    solved_latest_date= models.DateField(auto_now=True, null=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

# 履歴テーブル
class History(models.Model):
    solved_date = models.DateField(auto_now=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)