from django.http import HttpResponse
from django.shortcuts import redirect

from .models import Token


def get_full_url(short_url: str) -> str:
    """Поиск длинной ссылки в базе по короткой. Возврат и обработка ошибки."""
    try:
        token = Token.objects.get(short_url__exact=short_url)
    except Token.DoesNotExist:
        raise KeyError('For this short URL there is no full URL.')

    return token.full_url


def redirection(request, short_url):
    """Перенаправление пользователя по длинной ссылке."""
    try:
        full_link = get_full_url(short_url)
        return redirect(full_link)
    except Exception as exp:
        return HttpResponse(exp.args)  # Что-то пошло не так.
