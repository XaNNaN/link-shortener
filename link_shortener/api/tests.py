from django.test import TestCase
from rest_framework.test import APITestCase

from .models import Token


class TestAPI(APITestCase):
    """Тестируем POST запросы"""
    url = '/api/tokens/'

    def test_token_create(self):
        """
        Проверка создания токена без явного указания короткой ссылки
        и с явным указанием короткой ссылки
        """
        creation_data = {
            'full_url': 'http://post.url.test.ru'
        }

        response_create = self.client.post(self.url, data=creation_data)
        result_create = response_create.json()

        self.assertEqual(response_create.status_code, 201)
        self.assertEqual(result_create['full_url'], 'http://post.url.test.ru')
        self.assertIsInstance(result_create, dict)



class TestRedirection(TestCase):
    """Тестируем GET запросы"""
    active_url = '/aEdj01'
    deactive_url = '/q2Nb23'

    def setUp(self) -> None:
        Token.objects.create(
            full_url='https://ya.ru/',
            short_url='aEdj01',
        )

        Token.objects.create(
            full_url='https://stackoverflow.com/',
            short_url='q2Nb23',
            is_active=False
        )

    def test_redirection(self):
        """Тестируем переадресацию"""
        response = self.client.get(self.active_url)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, 'https://ya.ru/')

    def test_response_counter(self):
        """Тестируем счетчик запросов токена"""
        self.assertEqual(
            Token.objects.get(short_url='aEdj01').requests_count, 0
        )
        self.client.get(self.active_url)
        self.assertEqual(
            Token.objects.get(short_url='aEdj01').requests_count, 1
        )
        self.assertEqual(
            Token.objects.get(short_url='q2Nb23').requests_count, 0
        )
        self.client.get(self.deactive_url)
        self.assertEqual(
            Token.objects.get(short_url='q2Nb23').requests_count, 0
        )

    def test_deactive_url(self):
        """Тестируем неактивные токены"""
        response = self.client.get(self.deactive_url)
        self.assertEqual(response.content, b'Token is no longer available')