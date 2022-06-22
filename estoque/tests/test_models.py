from django.test import TestCase
from estoque.models import Produto, Fornecedor, Entrada, Saida

class TestModels(TestCase):

  def setUp(self):
    # Cria um Produto no banco de dados
    self.produto = Produto(nome='Produto 1', estoque=10, consumo_medio=1, estoque_minimo=5, estoque_maximo=15)
    self.produto.save()

    # Cria um Fornecedor no banco de dados
    self.fornecedor = Fornecedor(nome='Fornecedor Teste', telefone='123456789', lead_time=1, entrega_segunda=True, entrega_terca=True, entrega_quarta=True, entrega_quinta=True, entrega_sexta=True, entrega_sabado=True, entrega_domingo=True)
    self.fornecedor.save()


  def test_criacao_produto(self):

    # Verifica se o Produto foi criado corretamente
    self.assertTrue(Produto.objects.exists())
    self.assertEqual(Produto.objects.count(), 1)
    self.produto_criado = Produto.objects.first()
    self.assertEqual(self.produto_criado.nome, 'Produto 1')
    self.assertEqual(self.produto_criado.estoque, 10)
    self.assertEqual(self.produto_criado.consumo_medio, 1)
    self.assertEqual(self.produto_criado.estoque_minimo, 5)
    self.assertEqual(self.produto_criado.estoque_maximo, 15)

  def test_criacao_fornecedor(self):

    # Verifica se o Fornecedor foi criado corretamente
    self.assertTrue(Fornecedor.objects.exists())
    self.assertEqual(Fornecedor.objects.count(), 1)
    self.fornecedor_criado = Fornecedor.objects.first()
    self.assertEqual(self.fornecedor_criado.nome, 'Fornecedor Teste')
    self.assertEqual(self.fornecedor_criado.telefone, '123456789')
    self.assertEqual(self.fornecedor_criado.lead_time, 1)
    self.assertEqual(self.fornecedor_criado.entrega_segunda, True)
    self.assertEqual(self.fornecedor_criado.entrega_terca, True)
    self.assertEqual(self.fornecedor_criado.entrega_quarta, True)
    self.assertEqual(self.fornecedor_criado.entrega_quinta, True)
    self.assertEqual(self.fornecedor_criado.entrega_sexta, True)
    self.assertEqual(self.fornecedor_criado.entrega_sabado, True)
    self.assertEqual(self.fornecedor_criado.entrega_domingo, True)

  def test_criacao_entrada(self):
    self.produto_criado = Produto.objects.first()
    self.fornecedor_criado = Fornecedor.objects.first()
    
    # Cria uma Entrada no banco de dados
    self.entrada = Entrada(produto=self.produto_criado, fornecedor=self.fornecedor_criado, quantidade=10, preco=10)
    self.entrada.save()

    # Verifica se a Entrada foi criada corretamente
    self.assertTrue(Entrada.objects.exists())
    self.assertEqual(Entrada.objects.count(), 1)
    self.entrada_criada = Entrada.objects.first()
    self.assertEqual(self.entrada_criada.produto, self.produto_criado)
    self.assertEqual(self.entrada_criada.fornecedor, self.fornecedor_criado)
    self.assertEqual(self.entrada_criada.quantidade, 10)
    self.assertEqual(self.entrada_criada.preco, 10)

  def test_criacao_saida(self):
    self.produto_criado = Produto.objects.first()
    self.fornecedor_criado = Fornecedor.objects.first()
    
    # Cria uma Saída no banco de dados
    self.saida = Saida(produto=self.produto_criado, quantidade=1)
    self.saida.save()

    # Verifica se a Saída foi criada corretamente
    self.assertTrue(Saida.objects.exists())
    self.assertEqual(Saida.objects.count(), 1)
    self.saida_criada = Saida.objects.first()
    self.assertEqual(self.saida_criada.produto, self.produto_criado)
    self.assertEqual(self.saida_criada.quantidade, 1)