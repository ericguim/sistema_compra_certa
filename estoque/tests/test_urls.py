from django.test import SimpleTestCase
from django.urls import reverse, resolve
from estoque.views import estoque

class TestUrls(SimpleTestCase):

  # Testa se a url de estoque está correta
  def test_estoque_url_resolves(self):
    url = reverse('estoque')
    self.assertEquals(resolve(url).func, estoque)
  