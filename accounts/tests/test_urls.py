from django.test import SimpleTestCase
from django.urls import reverse, resolve
from accounts.views import login

class TestUrls(SimpleTestCase):

  # Testa se a url de login está correta
  def test_login_url_resolves(self):
    url = reverse('login')
    self.assertEquals(resolve(url).func, login)
  