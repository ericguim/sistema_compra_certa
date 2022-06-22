from django.test import SimpleTestCase
from django.urls import reverse, resolve
from entrada.views import entrada

class TestUrls(SimpleTestCase):

  # Testa se a url de entrada está correta
  def test_entrada_url_resolves(self):
    url = reverse('entrada')
    self.assertEquals(resolve(url).func, entrada)
  