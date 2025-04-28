from django.db import models

# Create your models here.

# カスタマーテーブル
# class CustomUser(models.Model):
#   username = models.CharField(max_length=30)
#   mail = models.EmailField(max_length=254)
#   password = models.CharField(max_length=255)


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