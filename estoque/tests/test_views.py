from urllib import response
from django.test import TestCase, Client
from django.urls import reverse
from estoque.models import Produto, Fornecedor
from django.contrib.auth.models import User

class TestViews(TestCase):

  def setUp(self):
    self.client = Client()
    self.estoque_url = reverse('estoque')

    # Cria um Produto no banco de dados
    self.produto = Produto(nome='Produto Teste', estoque=10, consumo_medio=1, estoque_minimo=5, estoque_maximo=15)
    self.produto.save()

    # Cria um Fornecedor no banco de dados
    self.fornecedor = Fornecedor(nome='Fornecedor Teste', telefone='123456789', lead_time=1, entrega_segunda=True, entrega_terca=True, entrega_quarta=True, entrega_quinta=True, entrega_sexta=True, entrega_sabado=True, entrega_domingo=True)
    self.fornecedor.save()

    # Cria um Usuario no banco de dados e loga no sistema
    self.user = User.objects.create_user(username='testuser', password='12345')
    self.client.login(username='testuser', password='12345')

  # Testa se a view estoque está correta
  def test_estoque_GET(self):
    self.produtos = Produto.objects.all()
    self.fornecedores = Fornecedor.objects.all()

    self.assertEquals(self.produtos.count(), 1)
    self.assertEquals(self.fornecedores.count(), 1)

    self.assertEquals(self.produtos[0].nome, 'Produto Teste')
    self.assertEquals(self.fornecedores[0].nome, 'Fornecedor Teste')

    response = self.client.get(self.estoque_url)
    self.assertEquals(response.status_code, 200)