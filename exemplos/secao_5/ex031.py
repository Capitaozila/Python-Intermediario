class Carrinho_de_compras:
  def __init__(self):
    self._produtos = []

  def total(self):
    return "R${:.2f}".format(sum([p.preco for p in self._produtos]))

  def inserir_produtos(self, *produtos):
    for produto in produtos:
      self._produtos.append(produto)

  def listar_produtos(self):
    print()
    for produto in self._produtos:
      print(produto.nome, "R${:.2f}".format(produto.preco))
    print()


class Produto:
  def __init__(self, nome, preco):
    self.nome = nome
    self.preco = preco


carrinho = Carrinho_de_compras()
p1, p2 = Produto("Caneta", 1.20), Produto("Camiseta", 89.90)
carrinho.inserir_produtos(p1, p2)
carrinho.listar_produtos()
print(carrinho.total())