from django.test import SimpleTestCase
from django.urls import reverse, resolve
from saida.views import saida

class TestUrls(SimpleTestCase):

  def test_saida_url_resolves(self):
    url = reverse('saida')
    self.assertEquals(resolve(url).func, saida)
  