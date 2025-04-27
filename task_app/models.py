from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

# カスタマーテーブル
class CustomUser(models.Model):
  username = models.CharField(max_length=30)
  mail = models.EmailField(max_length=254)
  password = models.CharField(max_length=255)


# カテゴリーテーブル
class Category(models.Model):
  OPTION_CHOICES = [
    ("1", "Python"),
    ("2", "CSS"),
    ("3", "JavaScript"),
    ("4", "TypeScript"),
    ("5", "Java"),
    ("6", "C"),
    ("7", "C#"),
    ("8", "C++"),
    ("9", "Go"),
  ]
  category_name = models.CharField(max_length=50, choices=OPTION_CHOICES)

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