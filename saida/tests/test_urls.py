from django.test import SimpleTestCase
from django.urls import reverse, resolve
from saida.views import saida

class TestUrls(SimpleTestCase):

  # Testa se a url de saida está correta
  def test_saida_url_resolves(self):
    url = reverse('saida')
    self.assertEquals(resolve(url).func, saida)
  