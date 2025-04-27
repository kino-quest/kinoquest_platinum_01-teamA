from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    first_name = None
    last_name = None
    email = models.EmailField(unique=True)

    def __str__(self):
        # 開発用にemailも表示する
        return f"{self.username} {self.email}"
    