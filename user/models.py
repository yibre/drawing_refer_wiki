from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email=models.EmailField(
        unique=True,
    )
    nickname = models.CharField(
        max_length=30,
        blank=True,
        default="",
    )

    class Meta:
        db_table = 'user'

