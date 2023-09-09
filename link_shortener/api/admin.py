from django.contrib import admin

from .models import Token


@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):
    list_display = (  # Список отображаемых полей
        'full_url',
        'short_url',
        'created_date',
        'is_active',
    )
    search_fields = ('full_url', 'short_url')
