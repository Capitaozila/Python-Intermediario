# @property + @setter - getter e setter no modo Pythônico
# @property - permite que o método seja acessado como um atributo
# @setter - permite que o atributo seja alterado
# p/ evitar quebrar o código do cliente
# p/ habilitar o setter
# p/ executar ações ao obter um atributo
# atributos que começam com 1 ou 2 underlines são privados, e não devem ser usados fora da classe
# aqui vai um exemplo com a classe Animal


class Animal:
  
  def __init__(self):
    self.__nome = 'Cachorro'
    self.__idade = 5
    self.__humano = False


animal1 = Animal()
print(animal1.__dict__)
print(animal1._Animal__nome)
print(animal1._Animal__idade)
print(animal1._Animal__humano)
# print(animal1.__nome)  # AttributeError
