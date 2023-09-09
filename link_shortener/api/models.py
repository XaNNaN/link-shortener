from hashlib import shake_128

from django.db import models
from django.conf import settings


class Token(models.Model):
    """Модель для хранения токенов"""
    full_url = models.URLField(unique=True)
    short_url = models.CharField(
        max_length=70,  # Максимальная длина ссылки согласно требованиям к СМС
        unique=True,
        db_index=True,
        blank=True,
    )
    created_date = models.DateTimeField(auto_now_add=True)  # Позже можно будет удалять ссылки, когда "посылка" получена
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        # Хешируем длинную ссылку
        self.short_url = shake_128(str(self.full_url).encode("utf-8")).hexdigest(3).upper()  # Не уверен в URLField

        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f'{self.short_url} -> {self.full_url}'

