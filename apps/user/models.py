from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # 추가적인 필드가 필요하면 여기서 정의
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username