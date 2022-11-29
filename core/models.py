from django.contrib.auth.models import AbstractUser
from django.db import models


class TelegramProfile(models.Model):
    id = models.IntegerField(
        null=False,
        unique=True,
        primary_key=True,
    )

class User(AbstractUser):
    telegram_profile = models.ForeignKey(
        TelegramProfile,
        null=True,
        on_delete=models.DO_NOTHING,
    )


