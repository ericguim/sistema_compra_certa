from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):

  def setUp(self):
    self.client = Client()
    self.login_url = reverse('login')

  # Testa se o viewl login está correto
  def test_accounts_POST(self):

    response = self.client.post(self.login_url, {'username': 'teste', 'password': 'teste'})
    self.assertEqual(response.status_code, 302)