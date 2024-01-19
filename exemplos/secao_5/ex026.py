class Animal:
    def __init__(self, nome):
        self.nome = nome

        variavel = 'valor'
        print(variavel)
    
    def comendo(self, alimento):
        return f'{self.nome} está comendo um(a) {alimento}'
    
    def executar(self, *agrs, **kwargs):
        return self.comendo(*agrs, **kwargs)

leao = Animal(nome='Leão')
print(leao.nome)
print(leao.executar('maçã'))

